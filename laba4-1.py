from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np

# Определение множества точек
points = np.array([
    [6, 10],  # A1
    [10, 2],  # A2
    [8, -1],  # A3
    [5, -4],  # A4
    [-4, 0],  # A5
    [1, -8],  # A6
    [-10, -5] # A7
])

# Построение выпуклой оболочки
hull = ConvexHull(points)

# Визуализация
plt.plot(points[:, 0], points[:, 1], 'o')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

# Подписи точек
for i, txt in enumerate(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']):
    plt.annotate(txt, (points[i, 0], points[i, 1]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Convex Hull')
plt.show()
