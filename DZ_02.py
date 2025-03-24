import numpy as np
import matplotlib.pyplot as plt
# Генерация двух наборов случайных данных
x = np.random.rand(5)  # массив из 5 случайных чисел для оси X
y = np.random.rand(5)  # массив из 5 случайных чисел для оси Y
print("Набор данных X:", x)
print("Набор данных Y:", y)
# Создание диаграммы рассеяния
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', marker='o', s=100)  # s - размер маркеров
plt.title('Диаграмма рассеяния')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()