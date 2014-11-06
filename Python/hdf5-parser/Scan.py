import datetime
import numpy


class Scan:
    def __init__(self, start_time, stop_time, measurements):
        self.start_time = start_time
        self.stop_time = stop_time
        self.measurements = measurements

    def get_start_time(self):
        return self.start_time

    def get_stop_time(self):
        return self.stop_time

    def get_start_datetime(self):
        return datetime.datetime.fromtimestamp(self.start_time).strftime('%Y-%m-%d %H:%M:%S')

    def get_stop_datetime(self):
        return datetime.datetime.fromtimestamp(self.stop_time).strftime('%Y-%m-%d %H:%M:%S')

    def get_measurements(self):
        return self.measurements

    def get_max_measurement(self):
        return max(self.measurements)

    def get_min_measurement(self):
        return min(self.measurements)

    def get_avg_measurement(self):
        return numpy.mean(self.measurements)

    def to_avro(self):
        return dict({
            'start_time': self.start_time,
            'stop_time': self.stop_time,
            'measurements': self.measurements,
        })
