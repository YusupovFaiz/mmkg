import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Углы поворота в радианах
alpha = np.pi / 3  # π/3
beta = -np.pi / 6  # -π/6
gamma = 0          # 0

# Матрица аксонометрического ортогонального проектирования
axonometric_matrix = np.array([
    [np.sqrt(3)/2, 0, -1/2],
    [-np.sqrt(3)/4, 1/2, np.sqrt(3)/4],
    [0, 0, 0]
])

# Вершины тетраэдра
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Проекция вершин тетраэдра
projected_vertices = np.dot(vertices, axonometric_matrix.T)

# Построение тетраэдра
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Добавление вершин тетраэдра
ax.scatter(projected_vertices[:, 0], projected_vertices[:, 1], projected_vertices[:, 2])

# Соединение вершин линиями для создания рёбер тетраэдра
edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]
for edge in edges:
    ax.plot3D(*zip(*projected_vertices[edge]), color='k')

# Настройка осей
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение
plt.show()
