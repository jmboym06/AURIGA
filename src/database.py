import sqlite3
                    # df = await websocket.recv()
def database_add(datos, connection):

    cursor = connection.cursor()

    timestamp = datos["timestamp"]
    accel_x = datos["accel_x"]
    accel_y = datos["accel_y"]
    temp_1 = datos["temp_1"]
    temp_2 = datos["temp_2"]
    prox = datos["proximidad"]
    volt = datos["voltaje"]
    extra = datos["extra"]

    cursor.execute('INSERT OR IGNORE INTO TELEMETRIA (timestamp, accel_x, accel_y, temp_1, temp_2, proximidad, voltaje, extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',(timestamp, accel_x, accel_y, temp_1, temp_2, prox, volt, extra,))
    return()