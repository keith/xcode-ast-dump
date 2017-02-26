#!/usr/bin/env python

import argparse
import os
import subprocess
import sys


def swiftc_executable(environment=None):
    environment = environment or os.environ

    try:
        return environment["AST_SWIFTC"]
    except KeyError:
        pass

    try:
        developer_dir = environment["DEVELOPER_DIR"]
        toolchain = environment["TOOLCHAINS"].rsplit(".", 1)[-1]
        toolchain_path = toolchain + ".xctoolchain"
        return os.path.join(developer_dir, "Toolchains", toolchain_path,
                            "usr/bin/swiftc")
    except KeyError:
        return "swiftc"


def is_in_xcode(environment=None):
    environment = environment or os.environ
    return environment.get("TOOLCHAINS") is not None


def ast_command(swiftc, arguments):
    return [swiftc, "-dump-ast"] + arguments


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


def main():
    _, other_arguments = build_parser().parse_known_args()
    command = ast_command(swiftc_executable(), other_arguments)
    if is_in_xcode():
        print(" ".join(command))
        print("\nAST:\n")
        sys.stdout.flush()
    print(subprocess.check_output(command))
    if is_in_xcode():
        print("Exiting with 1 to stop the build")
        sys.exit(1)

if __name__ == "__main__":
    main()
