import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from RecordingSession import RecordingSession


if __name__ == '__main__':
    schema_file = 'recording_session.avsc'
    print '[Avro] Loading Schema'
    schema = avro.schema.parse(open(schema_file).read())
    print '[Avro] Schema Loaded Successfully'

    print '[Parser] Parsing File'
    filename = 'V:\CircleS7en\Source and Code\wincom_data\IITSO_DATA_UNCAL_201102101444.hdf5'
    session = RecordingSession(filename)
    print '[Parser] File Parsed Successfully'

    print '[Avro] Creating Avro File'
    writer = DataFileWriter(open("V:/CircleS7en/Source and Code/wincom_data/test.avro", "w"), DatumWriter(), schema)
    avro_fields = session.to_avro()

    writer.append(avro_fields)
    print '[Avro] Avro File Created Successfully'
    writer.close()

    print '[Complete]'