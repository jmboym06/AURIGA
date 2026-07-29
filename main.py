import json
import websocket
import sqlite3
import from src.create_db import createdb
import from src.database import database_add

connection = sqlite3.connect('aurigadb.sqlite')
cursor = connection.cursor()

createdb(connection)
connection.commit()

while TRUE:
    data = await websocket.recv()
    datos = json.loads(data)
    database_add(data, connection)
    connection.commit()