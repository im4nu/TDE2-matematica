import matplotlib.pyplot as plt
import numpy as np

original_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

angle_degrees = 45
pivot = np.array([0.5, 0.5])

angle_radians = np.radians(angle_degrees)
rotation_matrix = np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                            [np.sin(angle_radians), np.cos(angle_radians)]])
rotated_points = np.dot(original_points - pivot, rotation_matrix.T) + pivot

plt.figure(figsize=(8, 4))
plt.plot(*original_points.T, label='Objeto Original', marker='o')
plt.plot(*rotated_points.T, label='Objeto Rotacionado', marker='x')
plt.legend()
plt.grid(True)
plt.title('Rotação de um Objeto')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
