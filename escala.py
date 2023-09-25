import matplotlib.pyplot as plt
import numpy as np

original_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

scale_factor = 1.5
pivot = np.array([0.5, 0.5])

scaled_points = (original_points - pivot) * scale_factor + pivot

plt.figure(figsize=(8, 4))
plt.plot(*original_points.T, label='Objeto Original', marker='o')
plt.plot(*scaled_points.T, label='Objeto Escalado', marker='x')
plt.legend()
plt.grid(True)
plt.title('Escala de um Objeto')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
