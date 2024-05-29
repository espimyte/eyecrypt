#!/usr/bin/env python

import subprocess
import tempfile
from PIL import Image
import piexif

import warnings
from cryptography.hazmat.primitives.ciphers import Cipher, modes
from cryptography.hazmat.primitives.ciphers.algorithms import *
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

from encryption import *

def log_action(action, args):
    """
    Logs the given action. Helper command to help keep track of function process.
    """
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
    """
    Resizes a given hex string to match the given bit size.
    """
    target_length = int(bit_size/4)
    hex_length = len(hex)

    if (hex_length < target_length):
        diff = target_length - (hex_length % target_length)
        return hex + ('0'*diff)
    elif (hex_length > target_length):
        return hex[:target_length]

    return hex

def pad_bytes(bytes, bit_size):
    """
    Given bytes and a bit size, pads the data until it is divisible by the bit size.
    """
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

def get_mode(method_data, block_size, iv, nonce):
    """
    Returns the mode with the iv/nonce set to it, if applicable.
    """
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
        case Mode.NONE:
            mode = None
        case _:
            mode = modes.ECB()
    
    return mode

def encrypt_file(converted_image_path, encrypted_image_path, algo, key, iv, nonce):
    """
    Encrypts the file at the converted image path to the encrypted image path given the algorithm, key, iv, and nonce.
    """
    with open(converted_image_path, "rb") as converted_binary:
        method_data = encryption.methods.get(algo)
        algorithm = method_data.get('algorithm')

        key_size = method_data.get('key_size')
        block_size = method_data.get('block_size') if 'block_size' in method_data else 0

        key = resize_hex(key, key_size)
        key_bytes = bytes.fromhex(key)

        mode = get_mode(method_data, block_size, iv, nonce)

        converted_binary_bytes = converted_binary.read()
        if ('block_size' in method_data):
            converted_binary_bytes = pad_bytes(converted_binary_bytes, block_size)

        cipher = Cipher(algorithm(key_bytes), mode)
        encryptor = cipher.encryptor()
        result = encryptor.update(converted_binary_bytes) + encryptor.finalize()

        with open(encrypted_image_path, "wb") as binary_file:
            binary_file.write(result)

def convert_to_bmp(input_image_path, converted_image_path):
    """
    Converts an image to bmp.
    """
    try:
        img = Image.open(input_image_path)
        img.save(converted_image_path)
    except:
        raise Exception("Something went wrong while converting the image.")

def generate_comment(algo, key, iv, nonce):
    """
    Generates a comment with information about what parameters were used.
    """
    data = ['algorithm: {}'.format(algo), 'key: {}'.format(key)]
    method_data = encryption.methods.get(algo)
    mode = method_data.get('mode')

    match mode:
        case Mode.CBC | Mode.OFB | Mode.CFB:
            data.append('iv: {}'.format(iv))
        case Mode.CTR:
            data.append('nonce: {}'.format(nonce))
    
    return 'Made with EYECRYPT ('+', '.join(data)+')'

def generate_output(encrypted_image_path, output_image_path, algo, key, iv, nonce):
    """
    Generates an output file by converting it to the output image type and injecting parameter information into the EXIF data.
    """
    try:
        exif_ifd = {piexif.ExifIFD.UserComment: generate_comment(algo, key, iv, nonce).encode()}
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