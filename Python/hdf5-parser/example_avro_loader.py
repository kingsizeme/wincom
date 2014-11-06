from SessionFactory import SessionFactory

if __name__ == '__main__':
    avro_file = '<YOUR_FILE_NAME_HERE>'
    factory = SessionFactory()
    recording_session = factory.session_from_avro_file(avro_file)
    print('Bands Within File: {0}'.format(recording_session.get_band_count()))
    print(recording_session.get_band_summary())
