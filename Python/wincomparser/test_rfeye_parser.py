from SessionFactory import SessionFactory

file = 'V:/CircleS7en/Source and Code/wincom_data/RFeye_WiFiUS_IIT_TOWER_140407_002017.bin'

factory = SessionFactory()

session = factory.session_from_rfeye_file(file)
print(session.get_band_summary())
