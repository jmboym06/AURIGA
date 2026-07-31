import json

def paquete(datos):
    paquete = {"timestamp": datos["timestamp"],
        "imu": {"accel_x": datos["accel_x"],"accel_y": datos["accel_y"]},
        "temperature": {"sensor1": datos["temp_1"], "sensor2": datos["temp_2"]},
        "power": {"voltage": datos["voltaje"]},
        "distance": {"proximity": datos["proximidad"]}}

    return json.dumps(paquete)

async def send_data(dashboards, datos):

    data_env = paquete(datos)
    for dashboard in dashboards.copy():
        try:
            await dashboard.send(data_env)
        except:
            dashboards.discard(dashboard)