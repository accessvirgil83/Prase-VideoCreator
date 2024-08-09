import pandas as pd
import os
import csv
import requests
import json


with open("config.json") as f:
    config = json.load(f)

# Папка для сохранения загружаемых файлов
output_dir = config["output_dir"]
os.makedirs(output_dir, exist_ok=True)  # Создадим папку, если она не существует


with open(config["log"], 'a') as output_file:
    # Открываем CSV файл для чтения
    with open(config["csv_file"], 'r', newline='') as csv_file:
        # Читаем данные из CSV с помощью DictReader
        reader = csv.DictReader(csv_file)
        # Обрабатываем каждую строку в CSV
        for line_number, row in enumerate(reader, start=1):  # Используем line_number для нумерации строк
            # Получаем ссылки
            main_photo_link = row['Ссылка на главное фото']
            additional_photo_links = row['Ссылки на дополнительные фото']
            # Разбиваем дополнительные ссылки по строкам
            additional_links_list = additional_photo_links.split('\n')  # Замените '\n' на нужный разделитель
            # Убираем лишние пробелы к каждой ссылке
            additional_links_list = [link.strip() for link in additional_links_list]

            # Формируем строку для записи
            output_line = f"{main_photo_link}, " + ", ".join(additional_links_list) + "\n"
            # Записываем в файл
            output_file.write(output_line)

            # Загрузка главного фото
            os.makedirs(output_dir+"/"+str(line_number), exist_ok=True)
            response_main = requests.get(main_photo_link)
            if response_main.status_code == 200:  # Проверяем успешность запроса
                with open(os.path.join(output_dir+"/"+str(line_number), "1.jpg"), 'wb') as img_file:
                    img_file.write(response_main.content)  # Сохраняем контент как бинарный файл
            else:
                print(f"Не удалось загрузить главное фото по ссылке: {main_photo_link}")

            # Загрузка дополнительных фото
            for i, additional_link in enumerate(additional_links_list, start=1):
                response_additional = requests.get(additional_link)
                if response_additional.status_code == 200:  # Проверяем успешность запроса
                    with open(os.path.join(output_dir+"/"+str(line_number), f"{i+1}.jpg"), 'wb') as img_file:
                        img_file.write(response_additional.content)  # Сохраняем контент как бинарный файл
                else:
                    print(f"Не удалось загрузить дополнительное фото по ссылке: {additional_link}")

            os.system(f'ffmpeg -framerate 1/3 -i {output_dir}/{line_number}/%d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p {output_dir}/{line_number}/finalvideo.mp4')