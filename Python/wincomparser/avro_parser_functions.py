import fastavro


def open_avro_file(file_path):
    # Abandon all hope ye who change from binary read
    # Seriously, don't it causes encoding errors everywhere
    reader = fastavro.iter_avro(open(file_path, "rb"))
    avro_dictionary = reader.next()
    return avro_dictionary



