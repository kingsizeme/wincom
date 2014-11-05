import h5py
from Band import Band


def open_hdf_file(filename):
    data_file = h5py.File(filename, 'r')
    return data_file


def parse_file(data_file):
    file_data = get_all_bands(data_file)

    all_data = get_all_data(data_file)
    all_scan_times = get_all_scan_times(data_file)
    for scan_id, complete_sweep in enumerate(all_data):
        for band_id, scan in enumerate(complete_sweep):
            start_time = all_scan_times[scan_id][0][band_id]
            end_time = all_scan_times[scan_id][1][band_id]
            file_data[band_id].add_scan(start_time, end_time, scan)

    return file_data


def get_all_data(data_file):
    data_group = data_file['/data']

    all_data = []
    for row in data_group:
        all_data.append(row[3])

    return all_data


def get_all_scan_times(data_file):
    data_group = data_file['/data']

    all_scan_times = []
    for row in data_group:
        all_scan_times.append([row[0], row[1]])

    return all_scan_times


def get_all_bands(data_file):
    bands_group = data_file['/bands']

    all_bands = []
    for row in bands_group:
        current_band = Band(row[1], row[2], row[3])
        all_bands.append(current_band)

    return all_bands


def get_scan_times(data_file):
    data_group = data_file['/data']

    # [Dictionary] scan_times = [Integer] Scan ID : [Tuple] (Start Time, End Time)
    scan_times = dict()
    scan_id = 0
    for row in data_group:
        time_entry = row[0], row[1]
        scan_times[scan_id] = time_entry
        scan_id += 1

    return scan_times


def get_scan_count(data_file):
    data_group = data_file['/data']
    return len(data_group)
