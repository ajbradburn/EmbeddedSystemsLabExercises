#!/usr/bin/python3

import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print('output_with_format.py -i <file_name>')
        sys.exit(2)

    input_file = ''

    for opt, arg in opts:
        if opt == '-h':
            print('output_with_format.py -i <file_name>')
        elif opt in ("-i"):
            input_file = arg

    try:
        open(input_file, "r")
    except IOError:
        print("Error: File does not exist?")
        return 0

        # We need to know what padding to apply.
    lines = []
    with open(input_file, "r") as f:
        lines = f.readlines()
    f.close()

    line_count = len(lines)

    padding = len("{}".format(line_count))
    fstring = "{:>" + str(padding) + "}|  {}"

    for i, line in enumerate(lines):
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        print(fstring.format(i+1, line.rstrip()))

if __name__ == "__main__":
    main(sys.argv[1:])
