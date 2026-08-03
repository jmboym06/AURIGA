import json

def paquete(datos):                                                                 # Empaqueta los datos para un archivo JSON que lea el dashboard
    paquete = {"timestamp": datos["timestamp"],
        "imu": {"accel_x": datos["accel_x"],"accel_y": datos["accel_y"], "accel_z": datos["accel_y"], "gyro_x": datos["gyro_x"], "gyro_y": datos["gyro_y"], "gyro_z": datos["gyro_z"]},
        "temperature": {"sensor1": datos["temp_1"], "sensor2": datos["temp_2"]},
        "power": {"voltage": datos["voltaje"]},
        "distance": {"proximity": datos["proximidad"]},
        "extra": {"extra": datos["extra"]},
        "event": {"event": datos["event"]}}

    return json.dumps(paquete)                                                      # Convierte en JSON

async def send_data(dashboards, datos):

    data_env = paquete(datos)
    for dashboard in dashboards.copy():
        try:                                                # Envía los datos a cada dashboard conectada
            await dashboard.send(data_env)
        except:
            dashboards.discard(dashboard)                   # Si no se conecta a una, la descarta