import os

# Укажите путь к вашей папке с файлами
mypath = "./in"

# Получаем список файлов в папке
files = os.listdir(mypath)

# Переименовываем файлы, убирая "2024-04-27" из названия
for filename in files:
    if filename.startswith("2024-04-27 "):
        new_filename = filename.replace("2024-04-27 ", "")
        os.rename(os.path.join(mypath, filename), os.path.join(mypath, new_filename))