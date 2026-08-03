                    # df = await websocket.recv()
def database_add(datos, cursor):

    timestamp = datos["timestamp"]      # Extraemos los datos obtenidos en el JSON que manda el microcontrolador
    accel_x = datos["accel_x"]          # Se asignan a las variables determinadas
    accel_y = datos["accel_y"]
    accel_z = datos["accel_z"]
    gyro_x = datos["gyro_x"]
    gyro_y = datos["gyro_y"]
    gyro_z = datos["gyro_z"]
    temp_1 = datos["temp_1"]
    temp_2 = datos["temp_2"]
    prox = datos["proximidad"]
    volt = datos["voltaje"]
    extra = datos["extra"]
                                        # Se inserta a la database en la tabla creada
    cursor.execute('INSERT OR IGNORE INTO TELEMETRIA (timestamp, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, temp_1, temp_2, proximidad, voltaje, extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(timestamp, accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, temp_1, temp_2, prox, volt, extra,))
    return()