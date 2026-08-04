import sqlite3

def createdb(connection):
    cursor = connection.cursor()  

    cursor.executescript("DROP TABLE IF EXISTS TELEMETRIA;")    # Elimina cualquier registro anterior por si acaso
    cursor.executescript("""
        CREATE TABLE TELEMETRIA(
           timestamp         INTEGER PRIMARY KEY, 
           accel_x           FLOAT , 
           accel_y           FLOAT ,
           accel_z           FLOAT ,
           gyro_x            FLOAT ,
           gyro_y            FLOAT ,
           gyro_z            FLOAT ,
           temp_1            FLOAT ,
           temp_2            FLOAT ,
           proximidad        FLOAT ,
           voltaje           FLOAT ,
           event             STRING ,
           extra             FLOAT );""")                        # Crea la tabla con las columnas determinadas
    return()