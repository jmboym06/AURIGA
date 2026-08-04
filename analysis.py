import pandas as pd
import numpy as np
from reporte.gg_scatter import gg_diag
from reporte.comparation import plot_filter
from reporte.report import generate_report
from reporte.errors import deteccion_fallo_imu

def analysis(csvf, csvr):
    try:                           # Carga el archivo al programa
        dataf = pd.read_csv(csvf)
        datar = pd.read_csv(csvr)
    except:
        print("No se encontró el archivo")

    dataf["accel_mag"] = np.sqrt(dataf["accel_x"]**2 + dataf["accel_y"]**2)      # Teorema de pitágoras
    max_G_force = dataf["accel_mag"].max()     # Calcula la magnitud de la aceleración en cada instante

    plot_filter(datar, dataf, "accel_x")     # Visualizamos la diferencia entre los datos crudos y los datos filtrados con graficas
    plot_filter(datar, dataf, "accel_y")

    gg_diag(dataf)                           # Genera el diagrama GG

    error_imu = dict()
    error_imu["accel_x"] = deteccion_fallo_imu(datar, "accel_x")     # Se detecta si hubo un fallo del IMU para las columnas seleccionadas
    error_imu["accel_y"] = deteccion_fallo_imu(datar, "accel_y")
    error_imu["accel_z"] = deteccion_fallo_imu(datar, "accel_z")
    error_imu["gyro_x"] = deteccion_fallo_imu(datar, "gyro_x")
    error_imu["gyro_y"] = deteccion_fallo_imu(datar, "gyro_y")
    error_imu["gyro_z"] = deteccion_fallo_imu(datar, "gyro_z")

    generate_report(len(dataf), max_G_force, error_imu)  # Genera un reporte de lo realizado
