# AZ_03
### AZ03. Визуализация данных. Использование библиотеки Matplotlib. Создание диаграмм и графиков
---
Создадим небольшой кейс с использованием построения графиков.
#Создаём файл с ценами:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
# Импортируем модуль CSV
import csv
# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Firefox()

# URL страницы
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")
---
# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
   writer = csv.writer(file)
   writer.writerow(['Price'])  # Записываем заголовок столбца

 # Записываем цены в CSV файл
   for price in prices:
       writer.writerow([price.text])
# Закрытие драйвера
driver.quit()

Сейчас цены находятся в файле. Но всё написанное считается текстом. Нам нужно убрать нечисловую часть и преобразовать числа в числовой формат.

Создаём отдельный файл.
Отправляем Нейрокоту запрос:
✍🏻 Нужно обработать данные в csv файле, нужно убрать в конце каждой строчки ₽/мес. и преобразовать в тип данных число
Напиши код на Python
---
Вставляем и проверяем код:
import csv
def clean_price(price):
   # Удаляем "₽/мес." и преобразуем в число
   return int(price.replace(' ₽/мес.', '').replace(' ', ''))
# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'
with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
   reader = csv.reader(infile)
   writer = csv.writer(outfile)
   # Читаем заголовок и записываем его в новый файл
   header = next(reader)
   writer.writerow(header)

 # Обрабатываем и записываем данные строк
   for row in reader:
       clean_row = [clean_price(row[0])]
       writer.writerow(clean_row)
print(f"Обработанные данные сохранены в файл {output_file}")  
Создаём график:
Создаём новый файл.
Отправляем Нейрокоту запрос:
✍Нужно построить график гистограмму для получившихся цен из файла ”cleaned_prices.csv” с использованием модуля matplotlib

---
Вставляем и проверяем код:
import pandas as pd
import matplotlib.pyplot as plt
# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)
# Предположим, что столбец с ценами называется 'price'
prices = data['Price']
# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')  
# Мы можем изменить количество bin-ов по своему усмотрению
# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
# Показать гистограмму
plt.show()
