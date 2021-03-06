import avro.schema
from os import path
from avro_parser_functions import *
from hdf_parser_functions import *
from rfeye_parser_functions import *
from avro.io import DatumWriter
from avro.datafile import DataFileWriter
from RecordingSession import RecordingSession


class SessionFactory:
    def __init__(self):
        return

    def session_from_hdf_file(self, input_path):
        filename = self.filename_from_path(input_path)
        file_date = file_date_from_hdf_name(filename)
        location = location_from_hdf_name(filename)
        data_file = open_hdf_file(input_path)
        bands = parse_hdf_file(data_file)
        return RecordingSession(filename, file_date, location, bands)

    def session_from_rfeye_file(self, input_path):
        filename = self.filename_from_path(input_path)
        file_date = file_date_from_rfeye_name(filename)
        location = location_from_rfeye_name(filename)
        data_file = open_rfeye_file(input_path)
        bands = parse_rfeye_file(data_file)
        return RecordingSession(filename, file_date, location, bands)

    def session_from_avro_file(self, input_path):
        avro_dictionary = open_avro_file(input_path)
        return self.from_avro(avro_dictionary)

    def from_avro(self, fields):
        filename = fields['filename']
        location = fields['location']
        file_date = fields['date']
        bands = []

        for band in fields['bands']:
            band_object = Band(band['start_freq'], band['stop_freq'], band['resolution'])
            for scan in band['scans']:
                band_object.add_scan(scan['start_time'], scan['stop_time'], scan['measurements'])
            bands.append(band_object)

        return RecordingSession(filename, file_date, location, bands)

    def save_as_avro_file(self, output_file, session):
        schema_file = 'recording_session.avsc'
        schema = avro.schema.parse(open(schema_file).read())
        avro_fields = session.to_avro()

        # Do not, I repeat, do not change this from binary write
        writer = DataFileWriter(open(output_file, "wb"), DatumWriter(), schema)
        writer.append(avro_fields)
        writer.close()

    def filename_from_path(self, filepath):
        return path.split(filepath)[1]