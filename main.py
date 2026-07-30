import json                                # Importa las librerias y funciones
import websockets
import sqlite3
import from src.create_db import createdb
import from src.database import database_add
import from src.filtros import update 
from scipy.signal import butter, sosfilt_zi

connection1 = sqlite3.connect('aurigadb.sqlite') # Conectamos con el database para poder usarlo
cursor1 = connection1.cursor()                    # Cursor para editar la database
connection2 = sqlite3.connect('aurigadb_filt.sqlite') # Conectamos con el database para poder usarlo
cursor2 = connection2.cursor()   

createdb(connection1)                            # Crea la database y la tabla dentro de ella
connection1.commit()                             # Confirma el cambio

sos = butter(N=4, Wn=20, fs=200, btype="low", output="sos") # Calcula los parametros del filtro Butterworth
zi = sosfilt_zi(sos)                                        # Inicia la memoria del filtro

while TRUE:
    data = await websockets.recv()              # Conecta con el WebScoket para recibir los datos del microcontrolador
    datos = json.loads(data)                    # Traduce el archivo JSON para poderlo procesar 
    database_add(data, connection1)              # Añade los datos de ese pack de datos a la database
    connection1.commit()                         # Confirma el cambio

    datos["accel_x"] = filtros.imu_x.update(datos["accel_x"])                 # Se filtra cada uno dependiendo el sensor
    datos["accel_y"] = filtros.imu_y.update(datos["accel_x"])
    datos["temp_1"] = filtros.temperature1.update(datos["temp_1"])
    datos["temp_2"] = filtros.temperature2.update(datos["temp_2"])
    datos["proximidad"] = filtros.proximity.update(datos["proximidad"])
    datos["voltaje"] = filtros.voltage.update(datos["voltaje"])
    datos["extra"] = filtros.extra.update(datos["extra"])