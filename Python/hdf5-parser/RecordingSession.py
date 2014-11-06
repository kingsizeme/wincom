from parser_functions import *


class RecordingSession:
    def __init__(self, filepath):
        self.filename = filename_from_path(filepath)
        self.file_date = file_date_from_name(self.filename)
        data_file = open_hdf_file(filepath)
        self.bands = parse_file(data_file)

    def print_bands(self):
        for band in self.bands:
            print band.to_string()

    def get_band_count(self):
        return len(self.bands)

    def get_scan_count(self):
        return len(self.scan_times)

    def get_band_for_frequency(self, frequency):
        for band in self.bands:
            if band.contains_frequency(frequency):
                return band

        return None

    def to_avro(self):
        bands = []
        for band in self.bands:
            bands.append(band.to_avro())

        return dict({
            'filename': self.filename,
            'date': self.file_date,
            'bands': bands,
        })