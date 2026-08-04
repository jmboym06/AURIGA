import matplotlib.pyplot as plt

def plot_filter(raw_df, filtered_df, column):       # Crea una grafica que compare los datos originales con los filtrados 

    plt.figure(figsize=(12,6))      # Tamaño en la pantalla

    plt.plot(raw_df["timestamp"], raw_df[column], label="Original") # Primera gráfica

    plt.plot(filtered_df["timestamp"], filtered_df[column], label="Filtrada")   # Segunda gráfica

    plt.xlabel("Tiempo (s)")    # Ejes
    plt.ylabel(column)

    plt.title(f"Filtro Butterworth - {column}")     # Título

    plt.legend() # Etiqueta de curvas

    plt.grid(True)      # Cuadrícula

    plt.show()  # Muestra la grafica