from parser_functions import *


class RecordingSession:
    def __init__(self, filename):
        data_file = open_hdf_file(filename)
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