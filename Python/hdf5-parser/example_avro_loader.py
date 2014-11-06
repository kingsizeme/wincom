from SessionFactory import SessionFactory

if __name__ == '__main__':
    avro_file = 'V:/CircleS7en/Source and Code/wincom_data/test.avro'
    factory = SessionFactory()
    recording_session = factory.session_from_avro_file(avro_file)
    print 'Bands Within File: ' + recording_session.get_band_count()
