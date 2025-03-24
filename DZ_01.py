import numpy as np
import matplotlib.pyplot as plt
# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1)
plt.axvline(mean + std_dev, color='blue', linestyle='dashed', linewidth=1)
plt.axvline(mean - std_dev, color='blue', linestyle='dashed', linewidth=1)
plt.legend({'Среднее': mean, '±1 стандартное отклонение': std_dev})
plt.show()
