import sys

def parse_file(file):
    print "[Processing] Parsing file " + file


def parse_all_files(arguments):
    for file in arguments:
        parse_file(file)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print "[Error] You didn't include any arguments!\n" \
              "[Usage] python hdf_parser.py /your/file/here /another/file/here"
    else:
        parse_all_files(arguments)