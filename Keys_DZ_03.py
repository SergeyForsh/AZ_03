from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Указываем URL
url = "https://spb.cian.ru/snyat/"
driver.get(url)
time.sleep(5)  # Ждем загрузки страницы
# Поиск элементов с ценами
prices_elements = driver.find_elements(By.CSS_SELECTOR, "_33974c2b58--price--eWXUB")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
   writer = csv.writer(file)
   writer.writerow(['Price'])  # Записываем заголовок столбца

 # Записываем цены в CSV файл
   for price in prices:
       writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

def clean_price(price):
   # Удаляем "₽/мес." и преобразуем в число
   return int(price.replace(' ₽', '').replace(' ', ''))

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

"""Создаём график:
Создаём новый файл.
Отправляем Нейрокоту запрос:
✍Нужно построить график гистограмму для получившихся цен из файла ”cleanedd_prices.csv” 
с использованием модуля matplotlib
Вставляем и проверяем код:"""

# Загрузка данных из CSV-файла
file_path = 'cleanedd_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Загружаем CSV с заголовками
df = pd.read_csv("cleanedd_prices.csv")

# Преобразуем столбец price в числовой формат (убираем возможные пробелы и символы валюты)
df["Price"] = df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True).astype(float)

# Вычисляем среднее значение
average_price = df["Price"].mean()

print(f"Средняя цена: {average_price:.2f}")

# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')

# Мы можем изменить количество bin-ов по своему усмотрению
# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
# Показать гистограмму
plt.show()

