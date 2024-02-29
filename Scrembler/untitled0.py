


import matplotlib.pyplot as plt

# Задаємо дані для графіка (приклад)
# y_values = [1, 1, 0, 0, 1, 1, 0, 0, 1]
 
y_values = [1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,1 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,1 ,1 ,0 ,1 ,0 ,0 ,1]

# Створюємо список, де зберігатимемо координати точок для графіка
points = []

# Проходимося по значенням y та додаємо координати точок у список points
# Проходимося по значенням y та додаємо координати точок у список points
x = 0  # Початкова координата x
for i, y in enumerate(y_values):
    if y == 1:
        points.append((x, y))
        points.append((x + 0.5, 1))
        points.append((x + 0.5, 0))
        points.append((x + 1, 0))
        # points.append((x + 1, 1))
    else:
        if y == 0:
            points.append((x, y))
            points.append((x, -1))
            points.append((x + 0.5, -1))
            points.append((x + 0.5, 0))
            points.append((x + 1, 0))
        else:
            points.append((x, y))
            points.append((x + 0.5, -1))
            points.append((x + 0.5, 0))
            points.append((x + 1, 0))
            points.append((x + 1, y))
    x += 1  # Збільшуємо x для наступної точки
# Розбиваємо список points на координати x та y
x_coords, y_coords = zip(*points)

# Побудова графіка
plt.figure(figsize=(20, 4))  # Розмір графіка
plt.plot(x_coords, y_coords, marker='none', markersize=10)  # Побудова лінійного графіка з маркерами
plt.title('Rz перетворення')
plt.xlabel('t')
plt.ylabel('c(t)')

plt.ylim(-1.1, 1.1)  # Межі осі y

plt.yticks([-1, 0, 1])  # Позначки на осі y

# Add a vertical, red line at all integer values of x
for x_val in range(len(x_coords)):
    if x_coords[x_val] % 8 == 0:
        plt.axvline(x=x_coords[x_val], color='red', linestyle='--', linewidth=1)

plt.show()