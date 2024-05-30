#!/usr/bin/env python

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import argparse
from encryption import *
from eyecrypt import eyecrypt, is_valid_hex

def print_action(action, args):
    """
    Prints the current action to stdout.
    """
    print("{}".format(action))

def print_warning(warning):
    """
    Prints a warning to stderr.
    """
    print("{}".format(warning), file=sys.stderr)

def print_algorithms(algorithm_list):
    """
    Prints all supported algorithms.
    """
    print("Supported algorithms:")
    print("\n".join(algorithm_list))

def get_args():
    """
    Parses command arguments.
    """
    parser = argparse.ArgumentParser()

    # Information 
    parser.add_argument("-list", "--list", help="list all supported algorithms", required=False, action='store_true')

    # Required arguments: input and output file paths
    parser.add_argument("-in", "--input", help="input file path", required='-list' not in sys.argv)
    parser.add_argument("-out", "--output", help="output file path", required='-list' not in sys.argv)

    # Optionally specify encryption algorithm, initialization value, and key
    parser.add_argument("-algo", "--algorithm", help="encryption algorithm", required=False)
    parser.add_argument("-key", "--key", help="key", required=False)
    parser.add_argument("-iv", "--iv", help="initialization value", required=False)
    parser.add_argument("-nonce", "--nonce", help="nonce", required=False)

    return parser.parse_args()

def main():
    args = get_args()

    if (args.list):
        print_algorithms(encryption.methods.keys())
        return

    input_image_path = args.input
    output_image_path = args.output

    if (not os.path.isfile(input_image_path)):
        print_warning("Could not find input file.")
        return

    algo = defaults.ALGORITHM
    key = defaults.KEY
    iv = defaults.IV
    nonce = defaults.NONCE

    if args.algorithm:
        algo = args.algorithm
        if (algo not in encryption.methods):
            print_warning("Please enter a valid algorithm.")
            return
    if args.key:
        key = args.key
        if (not is_valid_hex(key)):
            print_warning("Please enter a valid hexadecimal for the key.")
            return
    if args.iv:
        iv = args.iv
        if (not is_valid_hex(iv)):
            print_warning("Please enter a valid hexadecimal for the iv.")
            return
    if args.nonce:
        nonce = args.nonce
        if (not is_valid_hex(nonce)):
            print_warning("Please enter a valid hexadecimal for the nonce.")
            return

    eyecrypt(input_image_path = input_image_path, output_image_path = output_image_path, algo = algo, key = key, iv = iv, nonce = nonce, log_action = print_action)

    print("{}".format("Finished! (Saved to "+output_image_path+")"))
    return

main()