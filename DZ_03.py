from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Chrome()

# URL страницы
url = 'https://pixel24.ru/vcd-96/catalog.html?utm_source=eLama-yandex&utm_medium=cpc&eLamautm_campaign=+%7C+%D0%A2%D0%9A+%D0%A4%D0%BE%D1%82%D0%BE%D0%B0%D0%BF%D0%BF%D0%B0%D1%80%D0%B0%D1%82%D1%8B+%7C+%D0%A4%D0%B8%D0%B4+%D0%AF%D0%BD%D0%B4%D0%B5%D0%BA%D1%81+%D0%9C%D0%B0%D1%80%D0%BA%D0%B5%D1%82+%7C+%D0%A0%D0%A4&utm_content=cid%7C109620144%7Cgid%7C5434041184%7Caid%7C16590327844%7Cadp%7Cno%7Cdvc%7Cdesktop%7Cpid%7C51186412170%7Crid%7C51186412170%7Cdid%7C51186412170%7Cpos%7Cpremium2%7Cadn%7Csearch%7Ccrid%7C0%7C&utm_term=---autotargeting&yclid=10146383374760542207'

driver.get(url)

time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.CSS_SELECTOR, ".card-product__price")

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
✍Нужно построить график гистограмму для получившихся цен из файла ”cleaned_prices.csv” 
с использованием модуля matplotlib

3. Вставляем и проверяем код:"""

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

# Предположим, что столбец с ценами называется 'price'
prices = data['Price']

# Загружаем CSV с заголовками
df = pd.read_csv("cleaned_prices.csv")

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