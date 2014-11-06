import sys
from RecordingSession import RecordingSession


def parse_file(input_file, output_file):
    print "[Processing] Parsing File " + input_file
    session = RecordingSession(input_file)
    print '[Processing] File Successfully Parsed'
    print '[Processing] Saving As Avro File ' + output_file
    session.save_as_avro_file(output_file)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print "[Error] You didn't include any arguments!\n" \
              "[Usage] python hdf_parser.py /your/input file/here /your/output file/here"
    else:
        parse_file(arguments[0], arguments[1])