#!/usr/bin/env python

import argparse
import subprocess


def ast_command(arguments):
    return ["swiftc", "-dump-ast"] + arguments


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-emit-dependencies", action="store_true")
    parser.add_argument("-emit-module", action="store_true")
    parser.add_argument("-emit-module-path")
    parser.add_argument("-c", action="store_true")
    parser.add_argument("-emit-objc-header", action="store_true")
    parser.add_argument("-emit-objc-header-path")
    parser.add_argument("-parseable-output", action="store_true")
    return parser

if __name__ == "__main__":
    _, other_arguments = build_parser().parse_known_args()
    command = ast_command(other_arguments)
    print(" ".join(command))
    print(subprocess.check_output(command))
