import json                                # Importa las librerias y funciones
import websockets
import asyncio
import sqlite3
from src.create_db import createdb
from src.database import database_add
from src.filtros import filtrado
from src.sender_dash import send_data
from analysis import analysis
import pandas as pd
from datetime import datetime

connection1 = sqlite3.connect('aurigadb.sqlite') # Conectamos con el database para poder usarlo
cursor1 = connection1.cursor()                    # Cursor para editar la database
connection2 = sqlite3.connect('aurigadb_filt.sqlite') # Conectamos con el database para poder usarlo
cursor2 = connection2.cursor()   

createdb(connection1)                            # Crea la database y la tabla dentro de ella
createdb(connection2) 
connection1.commit() 
connection2.commit()                             # Confirma el cambio

dashboards = set()

async def dashboard_handler(websocket):         # Añade las conexiones de dashboards al servidor
    dashboards.add(websocket)
    try:
        await websocket.wait_closed()           # Mantiene a los dashboards que sigan conectados y elimina los que no

    finally:
        dashboards.discard(websocket)


async def main_dash():
    async with websockets.serve(dashboard_handler, "0.0.0.0", 9000):      # Crea un servidor WebSocket que acepta conexiones desde cualquier interfaz de red
        print("Servidor Dashboard conectado")
        await asyncio.Future()                                  # Mantiene vivo el servidor

async def handler_micro(websocket_in):

    print("Cliente conectado al servidor")

    try:
        async for data in websocket_in:              # Conecta con el WebScoket para recibir los datos del microcontrolador
            print("Mensaje Recibido")
            print(repr(data))
            datos = json.loads(data)                    # Traduce el archivo JSON para poderlo procesar 
            print(f"JSON transformado:{datos}")

            database_add(datos, cursor1)              # Añade los datos de ese pack de datos a la database

            datosf = filtrado(datos)                           # Filtra los datos obtenidos con un filtro Butterworth determinado para cada sensor

            if datosf["accel_x"] > 0.2:                        # Determinamos el evento que está ocurriendo en base a los datos filtrados de la IMU 
                datosf["event"] = "Accelerating"
            elif datosf["accel_x"] < -0.2:
                datosf["event"] = "Braking"
            else:
                datosf["event"] = "None"

            if datosf["accel_y"] > 0.2:
                datosf["event"] += " & turning Left"
            elif datosf["accel_y"] < -0.2:
                datosf["event"] += " & turning Right"

            database_add(datosf, cursor2)              # Añade los datos de ese pack de datos a la database

            print(f"Datos filtrados: {datosf}")
            connection1.commit()                         # Confirma el cambio
            connection2.commit()

            await send_data(dashboards, datosf)       # Manda los datos al websocket del dashboard

    except Exception as e:
        print(f"Error [handler_micro]: {e}")      # Por si ocurre un error

    finally:
        print("Cliente desconectado")


async def main_micro():

    async with websockets.serve(handler_micro, "0.0.0.0", 8765):      # Crea un servidor WebSocket que acepta conexiones desde cualquier interfaz de red
        print("Servidor microcontrolador conectado")

        await asyncio.Future()                                  # Mantiene vivo el servidor

async def main():
    try:
        await asyncio.gather(main_micro(), main_dash())             # Para ejecutar ambos servidores a la vez
    finally:
        df1 = pd.read_sql_query("SELECT * FROM TELEMETRIA", connection2)

        csv_file_filt = f"TELEMETRIA/telemetria_filt_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"
        df1.to_csv(csv_file_filt, index=False)

        df2 = pd.read_sql_query("SELECT * FROM TELEMETRIA", connection1)

        csv_file_raw = f"TELEMETRIA/telemetria_raw_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv"
        df2.to_csv(csv_file_raw, index=False)

        print("CSV guardado correctamente")

        analysis(csv_file_filt, csv_file_raw)

        connection1.close()
        connection2.close()

asyncio.run(main())                                             # Corre el la función main