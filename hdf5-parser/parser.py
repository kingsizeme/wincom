import h5py

filename = 'C:\Users\ericf_000\Downloads\Example Data\IITSO_DATA_UNCAL_201111270000.hdf5'


def view_bands(file):
    bands_group = file['/bands']

    table = []
    for row in bands_group:
        table.append(row)

    for row in table:
        print(row)

    return


def view_data(file):
    data_group = file['/data']

    table = []
    for row in data_group:
        table.append(row)

    scan_number = 0
    records_to_print = 2
    print('start\t\t\tstop\t\t\tmax(power)')
    for row in table:
        print('Slice {0} - From Time: {1}, To Time: {2}, Bands: {3}'.format(scan_number, min(row[0]), max(row[1]), len(row[3])))
        if scan_number < records_to_print:
            for count in range(0, len(row[0]) - 1):
                print('{0}\t{1}\t{2}'.format(row[0][count], row[1][count], max(row[3][count])))
            if scan_number < records_to_print - 1:
                print('\n*********************************************\nstart\t\t\tstop\t\t\tmax(power)')
        scan_number += 1

    return


def get_band_name(file, band_number):
    band_group = file['/bands']
    return band_group[band_number][0]


def get_band_range(file, band_number):
    band_group = file['/bands']
    return '{0} GHz - {1} GHz'.format(band_group[band_number][1], band_group[band_number][2])


def get_data_for_band(file, band_number):
    band_data = []
    data_group = file['/data']
    for scan in data_group:
        band_data.append([scan[0][band_number], scan[1][band_number], scan[3][band_number]])
    return band_data


def view_band(file, band_number):
    band_name = get_band_name(file, band_number)
    band_data = get_data_for_band(file, band_number)
    band_range = get_band_range(file, band_number)
    print('Band Name: ' + band_name)
    print('Band Range: ' + band_range)
    print('Scan\t\tFrom Time\t\tTo Time\t\tMax Power')
    scan_count = 0
    power_max = -9999999
    power_min = 0
    for row in band_data:
        print('{0}\t{1}\t{2}\t{3}'.format(scan_count, row[0], row[1], max(row[2])))
        power_max = max(max(row[2]), power_max)
        power_min = min(min(row[2]), power_min)
        scan_count += 1
    print('Power Range: {0} to {1}'.format(power_min, power_max))
    return


def get_band_index_from_freq(file, frequency):
    band_group = file['/bands']
    index = 0
    for row in band_group:
        if row[1] <= frequency <= row[2]:
            return index
        index += 1
    return -1


if __name__ == '__main__':
    data_file = h5py.File(filename, 'r')
    band_index = get_band_index_from_freq(data_file, 200.00)
    view_band(data_file, band_index)