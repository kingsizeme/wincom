import avro.schema
from avro.io import DatumWriter
from avro.datafile import DataFileWriter

output_file = 'V:/CircleS7en/Source and Code/wincom_data/test2.avro'

schema_file = 'recording_session.avsc'
schema = avro.schema.parse(open(schema_file).read())
avro_fields = dict({
    'filename': 'test_filename.foo',
    'date': 'test_date',
    'location': 'IITSO',
    'bands': [
        dict({
            'start_freq': 200.0,
            'stop_freq': 300.0,
            'resolution': 20,
            'scans': [
                dict({
                    'start_time': 100.5,
                    'stop_time': 200.0,
                    'measurements': [200.1, 200.5, 201.3]
                })
            ]
        })
    ]
})

writer = DataFileWriter(open(output_file, "w"), DatumWriter(), schema)
writer.append(avro_fields)
writer.close()