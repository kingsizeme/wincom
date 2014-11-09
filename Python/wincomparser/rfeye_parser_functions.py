import re
import numpy as np
from Band import Band

EOF = int('0x55555555', 0)
RFEYE_DATE = np.dtype([('day', np.uint8), ('month', np.uint8), ('year', np.uint8), ('pad', np.uint8)])
RFEYE_TIME = np.dtype([('hours', np.uint8), ('minutes', np.uint8), ('seconds', np.uint8), ('centiseconds', np.uint8)])

DATA_TYPES = dict({
    'file_header': np.dtype([('version', np.int32), ('description', np.str_, 32)]),
    'block_header': np.dtype([('data_thread', np.int32), ('bytes_in_block', np.int32), ('data_type', np.int32)]),
    'block_trailer': np.dtype([('checksum', np.int32), ('eof_marker', np.int32)]),
    'data_type': dict({
        1: np.dtype([('place_holder', np.int32)]),
        40: np.dtype([('clock_date', RFEYE_DATE), ('clock_time', RFEYE_TIME), ('clock_nano', np.uint32),
                      ('gps_date', RFEYE_DATE), ('gps_time', RFEYE_TIME), ('position_fix', np.uint8),
                      ('satellites', np.uint8), ('heading', np.int16), ('latitude', np.int32), ('longitude', np.int32),
                      ('speed', np.int32), ('altitude', np.int32)]),
    }),
})

def open_rfeye_file(filepath):
    data_file = file(filepath, 'rb')
    return data_file


def parse_rfeye_file(data_file):
    header = _parse_file_header(data_file)
    data = _parse_data(data_file)


def _parse_file_header(data_file):
    data = np.fromfile(data_file, dtype=DATA_TYPES['header'], count=1)[0]
    return dict({
        'version': int(data[0]),
        'description': data[1]
    })


def _parse_data(data_file):
    data = []
    while True:
        data_block = dict()

        try:
            data_block['header'] = _parse_block_header(data_file)

            bytes_in_block = data_block['header']['bytes_in_block']
            data_type = data_block['header']['data_type']

            data_block['payload'] = _parse_block_payload(data_file, bytes_in_block, data_type)
            data_block['trailer'] = _parse_block_trailer(data_file)

            data.append(data_block)
        except EOFError:
            break

    return data


def _parse_block_header(data_file):
    data = np.fromfile(data_file, dtype=DATA_TYPES['block_header'], count=1)[0]
    return dict({
        'data_thread': int(data[0]),
        'bytes_in_block': int(data[1]),
        'data_type': int(data[2]),
    })


def _parse_block_trailer(data_file):
    data = np.fromfile(data_file, dtype=DATA_TYPES['block_trailer'], count=1)[0]
    return dict({
        'checksum': int(data[0]),
        'eof_marker': int(data[1]),
    })


def _parse_block_payload(data_file, bytes_in_block, data_type):
    block_payload = np.dtype([('throw_away', np.str_, bytes_in_block)])
    data = np.fromfile(data_file, dtype=block_payload, count=1)[0]
    return dict({
        'throw_away': data[0],
    })


def location_from_rfeye_name(filename):
    split_file = filename.split('_')
    return '{0}_{1}'.format(split_file[2], split_file[3])


def file_date_from_rfeye_name(filename):
    numbers = re.findall(r"\d+", filename)
    if len(numbers) == 0:
        return 'Unknown'
    else:
        return '20{0}'.format(numbers[0][:6])