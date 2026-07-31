import json                                # Importa las librerias y funciones
import websockets
import asyncio
import sqlite3
from src.create_db import createdb
from src.database import database_add
from src.filtros import filtrado
from src.sender_dash import send_data

connection1 = sqlite3.connect('aurigadb.sqlite') # Conectamos con el database para poder usarlo
cursor1 = connection1.cursor()                    # Cursor para editar la database
connection2 = sqlite3.connect('aurigadb_filt.sqlite') # Conectamos con el database para poder usarlo
cursor2 = connection2.cursor()   

createdb(connection1)                            # Crea la database y la tabla dentro de ella
createdb(connection2) 
connection1.commit() 
connection2.commit()                             # Confirma el cambio

dashboards = set()

async def dashboard_handler(websocket):

    dashboards.add(websocket)

    try:
        await websocket.wait_closed()

    finally:
        dashboards.discard(websocket)


async def main_dash():

    async with websockets.serve(dashboard_handler, "0.0.0.0", 9000):      # Crea un servidor WebSocket que acepta conexiones desde cualquier interfaz de red

        await asyncio.Future()                                  # Mantiene vivo el servidor

async def handler_micro(websocket_in):
    async for data in websocket_in:              # Conecta con el WebScoket para recibir los datos del microcontrolador
        try:
            datos = json.loads(data)                    # Traduce el archivo JSON para poderlo procesar 

            database_add(datos, cursor1)              # Añade los datos de ese pack de datos a la database

            datosf = filtrado(datos)                           # Filtra los datos obtenidos con un filtro Butterworth determinado para cada sensor

            database_add(datosf, cursor2)              # Añade los datos de ese pack de datos a la database

            connection1.commit()                         # Confirma el cambio
            connection2.commit()

            await send_data(dashboards, datosf)       # Manda los datos al websocket del dashboard

        except Exception as e:
            print(f"Error [handler_micro]: {e}")      # Por si ocurre un error



async def main_micro():

    async with websockets.serve(handler_micro, "0.0.0.0", 8765):      # Crea un servidor WebSocket que acepta conexiones desde cualquier interfaz de red

        await asyncio.Future()                                  # Mantiene vivo el servidor

async def main():
    await asyncio.gather(main_micro(), main_dash())             # Para ejecutar ambos servidores a la vez

asyncio.run(main())                                             # Corre el la función main