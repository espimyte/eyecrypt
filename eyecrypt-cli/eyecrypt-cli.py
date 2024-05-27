#!/usr/bin/env python

import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import argparse
from eyecrypt import DEFAULTS, eyecrypt

def print_action(action, args):
    print("\033[94m{}\033[00m".format(action))

def get_args():
    parser = argparse.ArgumentParser()

    # Required arguments: input and output file paths
    parser.add_argument("-in", "--input", help="input file path", required=True)
    parser.add_argument("-out", "--output", help="output file path", required=True)

    # Optionally specify encryption algorithm, initialization value, and key
    parser.add_argument("-algo", "--algorithm", help="encryption algorithm", required=False)
    parser.add_argument("-key", "--key", help="key", required=False)
    parser.add_argument("-iv", "--iv", help="initialization value", required=False)

    return parser.parse_args()

def main():
    args = get_args()

    input_image_path = args.input
    output_image_path = args.output

    # Default encryption parameters
    algo = DEFAULTS.algorithm
    key = DEFAULTS.key
    iv = DEFAULTS.iv

    if (args.algorithm):
        algo = args.algorithm
    if (args.key):
        key = args.key
    if args.iv:
        iv = args.iv

    eyecrypt(input = input_image_path, output = output_image_path, algo = algo, key = key, iv = iv, log_action = print_action)

    print("\033[92m{}\033[00m".format("Finished! (Saved to "+output_image_path+")"))
    return

main()