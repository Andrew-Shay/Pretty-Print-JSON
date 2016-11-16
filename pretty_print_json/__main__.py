#!/usr/bin/env python

import argparse
import json
import sys

__author__ = "Andrew Shay"
__version__ = "2.0.3"


def get_commands():
    parser = argparse.ArgumentParser(prog='ppj',
                                     description='Pretty Print JSON v{}'.format(__version__))

    parser.add_argument('path', help='Path to JSON file')
    parser.add_argument("-o", "--overwrite",
                        help="Overwrites original file with pretty JSON",
                        action="store_true")
    parser.add_argument("-f", "--file",
                        help="Write pretty JSON to specific file")

    commands = parser.parse_args()
    return commands


def main():
    return_code = 0

    commands = get_commands()

    try:
        with open(commands.path, "r") as f:
            json_file = f.read()
    except Exception as e:
        print("[ERROR] Unable to open file")
        print(e)
        return 2

    try:
        pretty_json = json.dumps(json.loads(json_file), sort_keys=True,
                                 indent=4, separators=(',', ': '))
    except Exception as e:
        print("[ERROR] Invalid JSON")
        print(e)
        return 5

    print(pretty_json)

    if commands.overwrite:
        try:
            with open(commands.path, "w") as f:
                f.write(pretty_json)
        except Exception as e:
            print("[ERROR] Unable to overwrite file")
            print(e)
            return_code = 3

    if commands.file:
        try:
            with open(commands.file, "w") as f:
                f.write(pretty_json)
        except Exception as e:
            print("[ERROR] Unable to write new file")
            print(e)
            return_code = 4

    return return_code


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
