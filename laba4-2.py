import matplotlib.pyplot as plt
import numpy as np

# Заданный полигон (координаты вершин)
polygon = np.array([
    [6, 10],  # A1
    [10, 2],  # A2
    [8, -1],  # A3
    [5, -4],  # A4
    [-4, 0],  # A5
    [1, -8],  # A6
    [-10, -5] # A7
])

# Уравнения хорд
eq1 = lambda x: (10/10) * x + 3/5
eq2 = lambda x: (10-2)/(10-6) * x + 35/6

# Выпуклые части
convex_parts = []

# Пересечение хорд с полигоном
for i in range(len(polygon)):
    x_vals = np.linspace(polygon[i][0], polygon[(i+1) % len(polygon)][0], 100)
    y_vals = eq1(x_vals)
    mask = (y_vals >= polygon[i][1]) & (y_vals <= polygon[(i+1) % len(polygon)][1])
    convex_parts.append(np.column_stack((x_vals[mask], y_vals[mask])))

    x_vals = np.linspace(polygon[i][0], polygon[(i+1) % len(polygon)][0], 100)
    y_vals = eq2(x_vals)
    mask = (y_vals >= polygon[i][1]) & (y_vals <= polygon[(i+1) % len(polygon)][1])
    convex_parts.append(np.column_stack((x_vals[mask], y_vals[mask])))

# Визуализация
plt.figure(figsize=(8, 6))
for part in convex_parts:
    plt.fill(part[:, 0], part[:, 1], alpha=0.5)

plt.plot(polygon[:, 0], polygon[:, 1], 'o-', label='Polygon')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Division of Polygon into Convex Parts using Chords')
plt.legend()
plt.grid(True)
plt.show()
