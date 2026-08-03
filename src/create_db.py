def createdb(connection):
    cursor = connection.cursor()        # Cursor para editar la database

    cursor.executescript('DROP TABLE IF EXISTS TELEMETRIA;')    # Elimina cualquier registro anterior por si acaso
    cursor.executescript('' \
        'CREATE TABLE TELEMETRIA('\
        '   timestamp         INTEGER PRIMARY KEY,' \
        '   accel_x           FLOAT ,' \
        '   accel_y           FLOAT ,' \
        '   accel_z           FLOAT ,' \
        '   gyro_x           FLOAT ,' \
        '   gyro_y           FLOAT ,' \
        '   gyro_z           FLOAT ,' \
        '   temp_1            FLOAT ,'\
        '   temp_2            FLOAT ,'\
        '   proximidad        FLOAT ,' \
        '   voltaje           FLOAT ,'\
        '   event           FLOAT ,'\
        '   extra             FLOAT );')                        # Crea la tabla con las columnas determinadas
    return()