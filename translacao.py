import matplotlib.pyplot as plt
import numpy as np

original_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

translation_vector = np.array([2, 2])

translated_points = original_points + translation_vector

plt.figure(figsize=(8, 4))
plt.plot(*original_points.T, label='Objeto Original', marker='o')
plt.plot(*translated_points.T, label='Objeto Transladado', marker='x')
plt.legend()
plt.grid(True)
plt.title('Translação de um Objeto')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
