def deteccion_fallo_imu(df, columna):       # Detecta la caída de un sensor a partir de recibir valores nulos por 10ms
    contador = 0        # Contará los resultados consecutivos para decir si pasaron más de 100ms
    val_n = 0           # Indice del valor a revisar por iteración

    error_starts = list()       # Listas para guardar el tiempo de inicio y final del error
    error_ends = list()

    start = 0

    for value in df[columna]:   # Analiza cada valor de la columna elegida
        if value == 0:              # Elegimos 0 como el valor determinado para asumir que el sensor se ha caído
            if start == 0:
                start = df["timestamp"][val_n]       # Guarda el momento del inicio del error

        else:
            if  val_n > 0 and start > 0:
                if df["timestamp"][val_n] - start >= 100:      # Si el conjunto de valores nulos duró 100ms o más, consideramos una caída
                    error_starts.append(start)     # Guarda el inicio guardado anterioirmente
                    error_ends.append(df["timestamp"][val_n - 1])   # Guarda el último valor nulo (final del error)
            start = 0    # Reinicia inicio de errores
        val_n += 1
    if val_n > 0:
        if df["timestamp"][val_n-1] - start >= 100:
            error_starts.append(df["timestamp"][start])     # Mismo procedimiento que anterioirmente pero para el caso en que se 
            error_ends.append(df["timestamp"][val_n - 1])   # termine el archivo en error

    error_times = (error_starts, error_ends)
    return error_times          # Regresa una lista de los inicios y los finales de los errores
        
