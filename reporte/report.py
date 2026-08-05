def generate_report(len_data, max_f_g, max_t1, max_t2, imu_errors):  # Datos de lo realizado en el proyecto
    
    with open("report.txt", "w") as report:             # Creación de un reporte genérico para enumerar lo realizado
        report.write("=========================================\n")
        report.write("REPORTE DEL ANÁLISIS DE DATA ACQUISITION\n")
        report.write("=========================================\n\n")
        report.write("Equipo: AURIGA Racing\n\n")
        report.write("-----------------------------------------\n")
        report.write("1. Dataframe\n")
        report.write("-----------------------------------------\n\n")
        report.write("El dataframe fue obtenido a partir\nde los datos obtenidos por los sensores y\nprocesador por el ESP-32.\n\n")
        report.write(f"Rondas de datos obtenidos: {len_data}\n")

        if len_data == 0:
            report.write("No se detectaron registros válidos\n\n")
        report.write("-----------------------------------------\n")
        report.write("2. Signal Filtering\n")
        report.write("-----------------------------------------\n\n")
        report.write("El dataframe fue filtrado usando un filtro\nButterworth sosfilt para eliminar el ruido.\n\n")
        report.write("Orden: 2\n")
        report.write("Cuttoff frequency: \n     IMU: 20Hz\n     Voltaje: 5 Hz \n     Temperatura: 0.5 Hz\n     Proximidad: 5 Hz\n     Campos Magnéticos: 5 Hz\n")
        report.write("Sampling frequency: \n     IMU: 200Hz\n     Voltaje: 50 Hz \n     Temperatura: 5 Hz\n     Proximidad: 30 Hz\n     Campos Magnéticos: 50 Hz\n\n")
        report.write("-----------------------------------------\n")
        report.write("3. Maximum G Force\n")
        report.write("-----------------------------------------\n\n")  
        report.write("Se calcula la magnitud de la fuerza G en todos\nlos puntos y se determina el valor máximo.\n\n")
        report.write(f"Fuerza máxima calculada: {max_f_g} G\n\n")      
        report.write("-----------------------------------------\n")
        report.write("4. IMU Failure Detection\n")
        report.write("-----------------------------------------\n\n")
        report.write("Se analizaron las series de datos\nseleccionadas del dataframe en busca de\ncaídas o errores de los sensores IMU.\n\n")
        report.write("Persistence threshold: 100 ms\n")
        report.write(f"Columnas analizadas: {len(imu_errors)}\n\n")
        for element in imu_errors:
            report.write("-----------\n")
            report.write(f"{element}\n")
            report.write("-----------\n")
            report.write(f"Eventos detectados: {len(imu_errors[element][0])}\n\n")
            if len(imu_errors[element][0]) == 0:
                report.write("Sin fallas detectadas\n\n")
            else:
                counter = 0
                for evento in imu_errors[element][0]:
                    report.write(f"Evento {counter + 1}:\n")
                    report.write(f"Inicio: {imu_errors[element][0][counter]}\n")
                    report.write(f"Final: {imu_errors[element][1][counter]}\n")
                    report.write(f"Duración: {imu_errors[element][1][counter] - imu_errors[element][0][counter]} s\n\n")
                    counter += 1
        report.write("-----------------------------------------\n\n")
        report.write("5. Critical Temperatures\n")
        report.write("-----------------------------------------\n\n")
        report.write("Se analizaron las series de datos\nseleccionadas del dataframe en busca de\nlos valores máximos de temperatura.\n\n")
        report.write(f"Temperatura máxima del sensor 1: {max_t1}\n")
        report.write(f"Temperatura máxima del sensor 2: {max_t2}\n\n")
        report.write("=========================================\n")
        report.write("FIN DEL REPORTE\n")
        report.write("=========================================\n\n")

    import os

    os.startfile("report.txt")