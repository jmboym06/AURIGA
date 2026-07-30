from scipy.signal import butter, sosfilt, sosfilt_zi

class ButterworthFilter:                # Plantilla del filtro

    def __init__(self, fs, fc, order):  # Constructor

        self.sos = butter(order, fc, fs=fs, output="sos")   # Construye el filtro, usa un output Second Order Sections

        self.zi = sosfilt_zi(self.sos)                      # Crea la memoria del filtro

    def update(self, value):            # Funcion para actualizar los datos tras filtrarlos

        filtered, self.zi = sosfilt(self.sos, [value], zi=self.zi)  # Filtra los datos basado en la memoria y el filtro determinado

        return filtered[0]              # Devuelve el primer y único valor filtrado

imu_x = ButterworthFilter(200,20)          # Se hacen las especificaciones para cada sensor
imu_y = ButterworthFilter(200,20) 
voltage = ButterworthFilter(20,3)
temperature1 = ButterworthFilter(10,1)
temperature2 = ButterworthFilter(10,1)
proximity = ButterworthFilter(20,3)
extra = ButterworthFilter(20,1)

def filtrado (datos):
    datos["accel_x"] = imu_x.update(datos["accel_x"])                 # Se filtra cada uno dependiendo el sensor
    datos["accel_y"] = imu_y.update(datos["accel_y"])
    datos["temp_1"] = temperature1.update(datos["temp_1"])
    datos["temp_2"] = temperature2.update(datos["temp_2"])
    datos["proximidad"] = proximity.update(datos["proximidad"])
    datos["voltaje"] = voltage.update(datos["voltaje"])
    datos["extra"] = extra.update(datos["extra"])