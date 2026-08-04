import matplotlib.pyplot as plt

def gg_diag(df):          # Genera el diagrama GG a partir del dataframe
    plt.figure(figsize=(8,8))       # Tamaño

    plt.scatter(df["accel_y"], df["accel_x"], s=2, alpha=0.5)   # Forma de la gráfica

    plt.xlabel("Lateral Acceleration (G)")          # Ejes
    plt.ylabel("Longitudinal Acceleration (G)")

    plt.title("G-G Diagram")    # Título

    plt.grid(True)      # Cuadricula

    plt.show()  # Muestra la grafica