#!/usr/bin/env python

import subprocess
import tempfile

class Algorithms():
    ECB = ["aes-128-ecb", "aes-192-ecb", "aes-256-ecb", "aria-128-ecb", "aria-192-ecb", "aria-256-ecb", "bf-ecb","camellia-128-ecb", "camellia-192-ecb", "camellia-256-ecb", "cast5-ecb", "des-ecb", "idea-ecb", "rc2-ecb", "rc5-ecb", "seed-ecb", "sm4-ecb"]
    CBC = ["aes-128-cbc", "aes-192-cbc", "aes-256-cbc", "aria-128-cbc", "aria-192-cbc", "aria-256-cbc", "bf-cbc", "camellia-128-cbc", "camellia-192-cbc", "camellia-256-cbc", "cast-cbc", "cast5-cbc", "des-cbc", "des-ede-cbc", "des-ede3-cbc", "idea-cbc", "rc2-40-cbc", "rc2-64-cbc", "rc2-cbc", "rc5-cbc", "seed-cbc", "sm4-cbc"]
    CFB = ["aria-128-cfb", "aria-128-cfb1", "aria-128-cfb8", "aria-192-cfb", "aria-192-cfb1", "aria-256-cfb8", "bf-cfb", "cast5-cfb", "des-cfb", "des-ede-cfb", "des-ede3-cfb", "idea-cfb", "rc2-cfb", "rc5-cfb", "seed-cfb", "sm4-cfb"]
    CTR = ["aria-128-ctr", "aria-192-ctr", "aria-256-ctr", "sm4-ctr"]
    OFB = ["aria-128-ofb", "aria-192-ofb", "aria-256-ofb", "bf-ofb", "cast5-ofb", "des-ede-ofb", "des-ofb", "idea-ofb", "rc2-ofb", "rc5-ofb", "seed-ofb", "sm4-ofb"]
    OTHER = ["base64", "bf", "cast", "des", "des-ede", "des-ede3", "des3", "desx", "idea", "rc2", "rc4", "rc4-40", "rc5", "seed"]

class Defaults():
    ALGORITHM = "aes-128-ecb"
    KEY = "00000000000000000000000000000000"
    IV = "0"

class Messages():
    NO_MAGICK = "ImageMagick could not be found. Please install ImageMagick and/or check if you have it installed correctly."
    NO_OPENSSL = "OpenSSL could not be found. Please install OpenSSL and/or check if you have it installed correctly."

algorithms = Algorithms()
defaults = Defaults()
messages = Messages()

def log_action(action, args):
    print("\033[94m{}\033[00m".format(action))

def check_installation(program):
    """
    Returns whether or not a program is installed.
    """
    cmd = program
    if (program == "openssl"):
        cmd = "openssl help"
    elif (program == "magick"):
        cmd = "magick -help"
    
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

def generate_encrypt_command(input, output, algo, key, iv):
    """
    Generates an encryption command given the algorithm, key, and input and output path.
    For algorithms that require an initialization value, a default value is used.
    """
    if (algo not in algorithms.ECB):
        return 'openssl enc -{algo} -e -K {key} -iv {iv} -in {input} -out {output}'.format(input = input, output = output, algo = algo, key = key, iv = iv)
    else:
        return 'openssl enc -{algo} -e -K {key} -in {input} -out {output}'.format(input = input, output = output, algo = algo, key = key)

def eyecrypt(input, output, algo = defaults.ALGORITHM, key = defaults.KEY, iv = defaults.IV, log_action = log_action, **kwargs):
    """
    Performs the process of converting and encrypting an image file given an input path, output path, key and algorithm.
    """
    
    input_image_path = "\""+input+"\""
    output_image_path = "\""+output+"\""

    # Generate temporary directory to store temp files in
    log_action(action = "Creating temp files...", args = kwargs)
    temp_directory = tempfile.TemporaryDirectory()
    converted_image_path = tempfile.NamedTemporaryFile(dir=temp_directory.name).name +".bmp"
    encrypted_image_path = tempfile.NamedTemporaryFile(dir=temp_directory.name).name +".bmp"

    # Convert image to bmp
    log_action(action = "Converting image to bmp...", args = kwargs)
    convert_cmd = 'magick {input} {output}'.format(input = input_image_path, output = converted_image_path)
    call_subprocess(convert_cmd, "Something went wrong while converting the image.")

    # Encrypt converted image
    log_action(action ="Encrypting converted image...", args = kwargs)
    encrypt_cmd = generate_encrypt_command(converted_image_path, encrypted_image_path, algo, key, iv)
    call_subprocess(encrypt_cmd, "Something went wrong while encrypting the image.")

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
    output_cmd = 'magick -define bmp:ignore-filesize=true {input} {output}'.format(input = encrypted_image_path, output = output_image_path)
    
    call_subprocess(output_cmd, "Something went wrong while generating the output image.")