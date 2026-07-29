import sqlite3
def createdb(connection):
    cursor = connection.cursor()

    cursor.executescript('DROP TABLE IF EXISTS TELEMETRIA;')
    cursor.executescript('' \
        'CREATE TABLE TELEMETRIA('\
        '   timestamp         INTEGER PRIMARY KEY,' \
        '   accel_x           FLOAT ,' \
        '   accel_y           FLOAT ,' \
        '   temp_1            FLOAT ,'\
        '   temp_2            FLOAT ,'\
        '   proximidad        FLOAT ,' \
        '   voltaje           FLOAT ,'\
        '   extra             FLOAT );')
    return()