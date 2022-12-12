#!/usr/bin/env python3

import getopt
import sys
import subprocess

argumentList = sys.argv[1:]

options = "hd"

long_options = ["help", "download"]

def usage():
    print('''Usage: [option...] [-h] [-d]
            -h, --help              Display this message and exit
            -d, --download          Download the selected media''')


def main():
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)

        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):
                usage()
            elif currentArgument in ("-d", "--download"):
                print ("Displaying file_name:", sys.argv[0])

    except getopt.error as err:
        print (str(err))

#TODO fix the checker

    # check if user has pip installed
    # if not subprocess.call("pip --version", shell=True):
        # print("pip is not installed")
        # exit(1)

    # check if user has virtualenv installed
    # if not subprocess.call("virtualenv --version", shell=True):
        # print("virtualenv is not installed")
        # exit(1)

    # check if user has python3 installed
    # if not subprocess.call("python3 --version", shell=True):
        # print("python3 is not installed")
        # exit(1)


if __name__ == "__main__":
    main()
