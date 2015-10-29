# ---------------------------------------------------------------------------
#   Author - Andrew Shay
#   Date: 10/28/2015
#   Description: Easy tool for printing pretty JSON
# ---------------------------------------------------------------------------

import sys
import json
import argparse

version = "1.0.1"


def get_commands():

    parser = argparse.ArgumentParser(prog='ppj',
                                     description='Prints pretty JSON')
    subparsers = parser.add_subparsers()

    p = subparsers.add_parser('p', help='Prints JSON file')
    p.set_defaults(which='p')
    p.add_argument('file_loc', help='Location of JSON file')
    p.add_argument("-o", "--overwrite",
                   help="Overwrites original file with pretty JSON",
                   action="store_true")
    p.add_argument("-f", "--file",
                   help="Write pretty JSON to specific file")

    version_subparser = subparsers.add_parser('version',
                                              help='Prints version')
    version_subparser.set_defaults(which='version')

    commands = parser.parse_args()
    return commands


def main():
    return_code = 0

    commands = get_commands()

    if commands.which == 'version':
        print("v" + version)
        return True

    if commands.which == 'p':

        try:
            json_file = open(commands.file_loc, "r").read()
        except Exception, e:
            print("[ERROR] Unable to open file")
            print(e)
            return 2

        try:
            pretty_json = json.dumps(json.loads(json_file), sort_keys=True,
                                     indent=4, separators=(',', ': '))
        except Exception, e:
            print("[ERROR] Invalid JSON")
            print(e)
            return 1

        print(pretty_json)

        if commands.overwrite:
            try:
                open(commands.file_loc, "w").write(pretty_json)
            except Exception, e:
                print("[ERROR] Unable to overwrite file")
                print(e)
                return_code = 3

        if commands.file is not None:
            try:
                open(commands.file, "w").write(pretty_json)
            except Exception, e:
                print("[ERROR] Unable to write new file")
                print(e)
                return_code = 4

    return return_code

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
