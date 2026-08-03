from scipy.signal import butter, sosfilt, sosfilt_zi

class ButterworthFilter:                # Plantilla del filtro

    def __init__(self, fs, fc, order):  # Constructor

        self.sos = butter(order, fc, fs=fs, output="sos")   # Construye el filtro, usa un output Second Order Sections

        self.zi = sosfilt_zi(self.sos)                      # Crea la memoria del filtro

    def update(self, value):            # Funcion para actualizar los datos tras filtrarlos

        filtered, self.zi = sosfilt(self.sos, [value], zi=self.zi)  # Filtra los datos basado en la memoria y el filtro determinado

        return filtered[0]              # Devuelve el primer y único valor filtrado

imu_x = ButterworthFilter(200,20,2)          # Se hacen las especificaciones para cada sensor
imu_y = ButterworthFilter(200,20,2) 
imu_z = ButterworthFilter(200,20,2) 
gyro_x = ButterworthFilter(200,20,2)          
gyro_y = ButterworthFilter(200,20,2) 
gyro_z = ButterworthFilter(200,20,2)
voltage = ButterworthFilter(50,5,2)
temperature1 = ButterworthFilter(5,0.5,2)
temperature2 = ButterworthFilter(5,0.5,2)
proximity = ButterworthFilter(30,5,2)
extra = ButterworthFilter(20,1,4)

def filtrado (datos):
    datos["accel_x"] = imu_x.update(datos["accel_x"])                 # Se filtra cada uno dependiendo el sensor
    datos["accel_y"] = imu_y.update(datos["accel_y"])
    datos["accel_z"] = imu_z.update(datos["accel_z"])                 
    datos["gyro_x"] = gyro_x.update(datos["gyro_x"])
    datos["gyro_y"] = gyro_y.update(datos["gyro_y"])
    datos["gyro_z"] = gyro_z.update(datos["gyro_z"])
    datos["temp_1"] = temperature1.update(datos["temp_1"])
    datos["temp_2"] = temperature2.update(datos["temp_2"])
    datos["proximidad"] = proximity.update(datos["proximidad"])
    datos["voltaje"] = voltage.update(datos["voltaje"])
    datos["extra"] = extra.update(datos["extra"])

    return datos