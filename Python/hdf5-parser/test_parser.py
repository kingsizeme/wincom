from RecordingSession import RecordingSession

def times_to_string(times):
    output = 'Times Occurred: {0}'.format(len(times))
    for instance, time in enumerate(times):
        output += '\n[{0}] Between {1} and {2}'.format(instance+1, time[0], time[1])
    return output

if __name__ == '__main__':
    filename = 'V:\CircleS7en\Source and Code\wincom_data\IITSO_DATA_UNCAL_201301020000.hdf5'
    session = RecordingSession(filename)
    band = session.get_band_for_frequency(5300)
    print band.to_string()

    max = band.get_max_recorded_power()
    max_times = band.get_datetimes_of_max()
    min = band.get_min_recorded_power()
    min_times = band.get_datetimes_of_min()

    print 'Maximum Power: {0} dB\n{1}'.format(max, times_to_string(max_times))
    print '\n'
    print 'Minimum Power: {0} dB\n{1}'.format(min, times_to_string(min_times))