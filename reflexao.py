import matplotlib.pyplot as plt
import numpy as np

original_points = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])

reflection_axis = 'x'

if reflection_axis == 'x':
    reflected_points = np.array(original_points) * np.array([1, -1])
elif reflection_axis == 'y':
    reflected_points = np.array(original_points) * np.array([-1, 1])
else:
    raise ValueError("Eixo de reflexão inválido. Use 'x' ou 'y'.")

plt.figure(figsize=(8, 4))
plt.plot(*original_points.T, label='Objeto Original', marker='o')
plt.plot(*reflected_points.T, label='Objeto Refletido', marker='x')
plt.legend()
plt.grid(True)
plt.title('Reflexão de um Objeto')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
