import sys
from SessionFactory import SessionFactory

def parse_hdf_file(input_file, output_file):
    print '[Processing] Creating Session Factory'
    factory = SessionFactory()

    print '[Processing] Parsing File ' + input_file
    session = factory.session_from_hdf_file(input_file)

    print '[Processing] File Successfully Parsed'
    print '[Processing] Saving As Avro File ' + output_file
    factory.save_as_avro_file(output_file, session)


if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print "[Error] You didn't include any arguments!\n" \
              "[Usage] python hdf_parser.py /your/input file/here /your/output file/here"
    else:
        parse_hdf_file(arguments[0], arguments[1])