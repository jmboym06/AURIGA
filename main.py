import json                                # Importa las librerias y funciones
import websockets
import sqlite3
from src.create_db import createdb
from src.database import database_add
from src.filtros import filtrado

url = ""
#async with websockets.connect(url) as websocket:

connection1 = sqlite3.connect('aurigadb.sqlite') # Conectamos con el database para poder usarlo
cursor1 = connection1.cursor()                    # Cursor para editar la database
connection2 = sqlite3.connect('aurigadb_filt.sqlite') # Conectamos con el database para poder usarlo
cursor2 = connection2.cursor()   

createdb(connection1)                            # Crea la database y la tabla dentro de ella
connection1.commit()                             # Confirma el cambio

while True:
    data = await websockets.recv()              # Conecta con el WebScoket para recibir los datos del microcontrolador
    datos = json.loads(data)                    # Traduce el archivo JSON para poderlo procesar 

    database_add(datos, cursor1)              # Añade los datos de ese pack de datos a la database

    filtrado(datos)                           # Filtra los datos obtenidos con un filtro Butterworth determinado para cada sensor

    database_add(datos, cursor2)              # Añade los datos de ese pack de datos a la database

    connection1.commit()                         # Confirma el cambio
    connection2.commit()
