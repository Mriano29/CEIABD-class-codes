import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos de la tabla
restaurantes = pd.DataFrame({
    "x": [2, 6, 8, 8, 12, 16, 20, 20, 22, 26],
    "y": [58, 105, 88, 118, 117, 137, 157, 169, 149, 202],
})

# Calculamos el valor de la recta de regresión lineal
# Promedio de x e y
promedio_x = restaurantes["x"].mean()
promedio_y = restaurantes["y"].mean()

# Pendiente -> b1
pendiente = np.sum((restaurantes["x"] - promedio_x) * (
    restaurantes["y"] - promedio_y)) / np.sum((restaurantes["x"] - promedio_x)**2)

# Intersección -> b0
interseccion = promedio_y - pendiente * promedio_x

# Estimaciones (la linea que sigue la recta)
estimaciones = interseccion + pendiente * restaurantes["x"]

# Graficar
plt.scatter(restaurantes["x"], restaurantes["y"],
            color='blue', label='Datos reales')
plt.plot(restaurantes["x"], estimaciones,
         color='red', label='Recta de regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regresión Lineal')
plt.legend()
plt.show()


# Coeficiente de determinación R2
SCT = np.sum((restaurantes["y"] - promedio_y)**2)
SCR = np.sum((estimaciones - promedio_y)**2)
R2 = SCR / SCT

# Coeficiente de correlación R
R = np.sqrt(R2)

print(f'Codeficiente de determinación R²: {R2}')
print(f'Codeficiente de correlacion R: {R}')
