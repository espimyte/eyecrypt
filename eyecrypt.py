#!/usr/bin/env python

import enum
import subprocess
import tempfile
from PIL import Image
import piexif

import warnings
from cryptography.hazmat import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.algorithms import *
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

class Mode(enum.Enum):
    ECB = 'ecb'
    CBC = 'cbc'
    CTR = 'ctr'
    OFB = 'ofb'
    CFB = 'cfb'

class Encryption():
    methods = {"aes-128-ecb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.ECB},
    "aes-192-ecb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.ECB},
    "aes-256-ecb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.ECB},
    "camellia-128-ecb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "camellia-192-ecb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "camellia-256-ecb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.ECB},
    "seed-ecb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.ECB},
    "sm4-ecb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.ECB},
    "cast5-ecb": {'algorithm': algorithms.CAST5, 'key_size': 128, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.ECB},
    "bf-ecb": {'algorithm': algorithms.Blowfish, 'key_size': 128, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.ECB},
    "idea-ecb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.ECB},
    "des3-ecb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.ECB},

    "aes-128-cbc": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CBC},
    "aes-192-cbc": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CBC},
    "aes-256-cbc": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CBC},
    "camellia-128-cbc": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "camellia-192-cbc": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "camellia-256-cbc": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CBC},
    "seed-cbc": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.CBC},
    "sm4-cbc": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CBC},
    "cast5-cbc": {'algorithm': algorithms.CAST5, 'key_size': 128, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.CBC},
    "bf-cbc": {'algorithm': algorithms.Blowfish, 'key_size': 128, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.CBC},
    "idea-cbc": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.CBC},
    "des3-cbc": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.CBC},

    "aes-128-ctr": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CTR},
    "aes-192-ctr": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CTR},
    "aes-256-ctr": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CTR},
    "camellia-128-ctr": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "camellia-192-ctr": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "camellia-256-ctr": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CTR},
    "sm4-ctr": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CTR},

    "aes-128-ofb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.OFB},
    "aes-192-ofb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.OFB},
    "aes-256-ofb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.OFB},
    "camellia-128-ofb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "camellia-192-ofb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "camellia-256-ofb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.OFB},
    "seed-ofb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.OFB},
    "sm4-ofb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.OFB},
    "cast5-ofb": {'algorithm': algorithms.CAST5, 'key_size': 128, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.OFB},
    "bf-ofb": {'algorithm': algorithms.Blowfish, 'key_size': 128, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.OFB},
    "idea-ofb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.OFB},
    "des3-ofb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.OFB},

    "aes-128-cfb": {'algorithm': algorithms.AES128, 'key_size': algorithms.AES128.key_size, 'block_size': algorithms.AES128.block_size, 'mode': Mode.CFB},
    "aes-192-cfb": {'algorithm': algorithms.AES, 'key_size': 192, 'block_size': algorithms.AES.block_size, 'mode': Mode.CFB},
    "aes-256-cfb": {'algorithm': algorithms.AES256, 'key_size': algorithms.AES256.key_size, 'block_size': algorithms.AES256.block_size, 'mode': Mode.CFB},
    "camellia-128-cfb": {'algorithm': algorithms.Camellia, 'key_size': 128, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "camellia-192-cfb": {'algorithm': algorithms.Camellia, 'key_size': 192, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "camellia-256-cfb": {'algorithm': algorithms.Camellia, 'key_size': 256, 'block_size': algorithms.Camellia.block_size, 'mode': Mode.CFB},
    "seed-cfb": {'algorithm': algorithms.SEED, 'key_size': 128, 'block_size': algorithms.SEED.block_size, 'mode': Mode.CFB},
    "sm4-cfb": {'algorithm': algorithms.SM4, 'key_size': 128, 'block_size': algorithms.SM4.block_size, 'mode': Mode.CFB},
    "cast5-cfb": {'algorithm': algorithms.CAST5, 'key_size': 128, 'block_size': algorithms.CAST5.block_size, 'mode': Mode.CFB},
    "bf-cfb": {'algorithm': algorithms.Blowfish, 'key_size': 128, 'block_size': algorithms.Blowfish.block_size, 'mode': Mode.CFB},
    "idea-cfb": {'algorithm': algorithms.IDEA, 'key_size': 128, 'block_size': algorithms.IDEA.block_size, 'mode': Mode.CFB},
    "des3-cfb": {'algorithm': algorithms.TripleDES, 'key_size': 64, 'block_size': algorithms.TripleDES.block_size, 'mode': Mode.CFB},
    }

class Defaults():
    ALGORITHM = "aes-128-ecb"
    KEY = "00000000000000000000000000000000"
    IV = "00000000000000000000000000000000"
    NONCE = "00000000000000000000000000000000"

encryption = Encryption()
defaults = Defaults()

def log_action(action, args):
    print("\033[94m{}\033[00m".format(action))

def is_valid_hex(str):
    """
    Returns whether or not a given string is a valid hexadecimal.
    """
    try:
        int(str, 16)
        return True
    except:
        return False
    
def resize_hex(hex, bit_size):
    target_length = int(bit_size/4)
    hex_length = len(hex)

    if (hex_length < target_length):
        diff = target_length - (hex_length % target_length)
        return hex + ('0'*diff)
    elif (hex_length > target_length):
        return hex[:target_length]

    return hex

def pad_bytes(bytes, bit_size):
    bytes_size = len(bytes)
    target_size = bit_size/8
    diff = int(target_size-int(bytes_size%target_size))
    bytes += b'\0'*(diff)

    return bytes

def check_installation(program):
    """
    Returns whether or not a program is installed.
    """
    cmd = program
    if (program == "openssl"):
        cmd = "openssl version"
    elif (program == "magick"):
        cmd = "magick -version"
    
    result = subprocess.call(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True)
    if (result == 0):
        return True
    else:
        return False

def call_subprocess(cmd, error_msg):
    """
    Calls the subprocess with a given command and raises an exception if there is an error.
    """
    return_code = subprocess.call(cmd, shell=True)
    if (return_code != 0):
        raise Exception(error_msg)

def get_mode(method_data, block_size, iv, nonce):
    iv = resize_hex(iv, block_size)
    iv_bytes = bytes.fromhex(iv)

    nonce = resize_hex(nonce, block_size)
    nonce_bytes = bytes.fromhex(nonce)

    match method_data.get('mode'):
        case Mode.ECB:
            mode = modes.ECB()
        case Mode.CBC:
            mode = modes.CBC(iv_bytes)
        case Mode.OFB:
            mode = modes.OFB(iv_bytes)
        case Mode.CFB:
            mode = modes.CFB(iv_bytes)
        case Mode.CTR:
            mode = modes.CTR(nonce_bytes)
        case _:
            mode = modes.ECB()
    
    return mode

def encrypt_file(converted_image_path, encrypted_image_path, algo, key, iv, nonce):
    with open(converted_image_path, "rb") as converted_binary:
        method_data = encryption.methods.get(algo)

        algorithm = method_data.get('algorithm')

        key_size = method_data.get('key_size')
        block_size = method_data.get('block_size')

        key = resize_hex(key, key_size)
        key_bytes = bytes.fromhex(key)

        mode = get_mode(method_data, block_size, iv, nonce)

        converted_binary_bytes = converted_binary.read()
        converted_binary_bytes = pad_bytes(converted_binary_bytes, block_size)

        cipher = Cipher(algorithm(key_bytes), mode)
        encryptor = cipher.encryptor()
        result = encryptor.update(converted_binary_bytes) + encryptor.finalize()

        with open(encrypted_image_path, "wb") as binary_file:
            binary_file.write(result)

def convert_to_bmp(input_image_path, converted_image_path):
    try:
        img = Image.open(input_image_path)
        img.save(converted_image_path)
    except:
        raise Exception("Something went wrong while converting the image.")

def generate_comment(algo, key, iv, nonce):
    data = ['algorithm: {algo}'.format(algo), 'key: {key}'.format(key)]
    method_data = encryption.methods.get(algo)
    mode = method_data.get('mode')

    match mode:
        case Mode.CBC | Mode.OFB | Mode.CFB:
            data.append('iv: {iv}'.format(iv))
        case Mode.CTR:
            data.append('nonce: {nonce}'.format(nonce))
    
    return 'Made with EYECRYPT ('+', '.join(data)+')'

def generate_output(encrypted_image_path, output_image_path, algo, key, iv, nonce):
    try:
        exif_ifd = {piexif.ExifIFD.UserComment: 'Made with EYECRYPT (algorithm: {algo}, key: {key}, iv: {iv}, nonce: {nonce})'.format( algo = algo, key = key, iv = iv, nonce = nonce).encode()}
        exif_dict = {"Exif": exif_ifd}
        exif_dat = piexif.dump(exif_dict)

        encrypted = Image.open(encrypted_image_path)
        encrypted.save(output_image_path,  exif=exif_dat)
    except:
        raise Exception("Something went wrong while generating the output image.")

def eyecrypt(input, output, algo = defaults.ALGORITHM, key = defaults.KEY, iv = defaults.IV, nonce = defaults.NONCE, log_action = log_action, **kwargs):
    """
    Performs the process of converting and encrypting an image file given an input path, output path, key and algorithm.
    """
    
    input_image_path = input
    output_image_path = output

    # Generate temporary directory to store temp files in
    log_action(action = "Creating temp files...", args = kwargs)
    temp_directory = tempfile.TemporaryDirectory()
    converted_image_path = tempfile.NamedTemporaryFile(dir=temp_directory.name).name +".bmp"
    encrypted_image_path = tempfile.NamedTemporaryFile(dir=temp_directory.name).name +".bmp"

    # Convert image to bmp
    log_action(action = "Converting image to bmp...", args = kwargs)
    convert_to_bmp(input_image_path, converted_image_path)

    # Encrypt converted image
    log_action(action ="Encrypting converted image...", args = kwargs)
    encrypt_file(converted_image_path, encrypted_image_path, algo, key, iv, nonce)

    # Read bmp header of converted image
    log_action(action ="Reading bmp header of converted image...", args = kwargs)
    converted_header = 0
    with open(converted_image_path, 'rb') as converted_file:
        converted_header = converted_file.read(54)
    
    # Overwrite bmp header of encrypted image
    log_action(action ="Overwriting bmp header of encrypted image...", args = kwargs)
    with open(encrypted_image_path, "r+b") as encrypted_file:
        encrypted_file.write(converted_header)

    # Generate output image
    log_action(action = "Generating output image...", args = kwargs)
    generate_output(encrypted_image_path, output_image_path, algo, key, iv, nonce)