import matplotlib.pyplot as plt
# x = [2, 3, 5, 8, 12, 13, 18]
# y = [1, 6, 9, 18, 20, 22, 25]
# plt.plot(x, y) #эта функция нужна для создания линейных графиков
# #Кастомизируем график, чтобы было понятно, где что. Даём графику название:
# plt.title("Пример простого линейного графика")
# plt.xlabel("x ось")
# plt.ylabel("y ось")
# plt.show()
print()
# data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 8, 8]
# #Создаём график частоты повторения. Указываем интервалы.
# plt.hist(data, bins=5)
# #Кастомизируем график:
# plt.xlabel("x ось")
# plt.ylabel("y ось")
# plt.title("Тестовая гистограма")
# plt.show()
print()
#Создаём диаграмму рассеяния:
x = [1, 4, 6, 7]
y = [3, 5, 8, 10]
plt.scatter(x, y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.title("Тестовая диаграмма рассеяния")
plt.show()