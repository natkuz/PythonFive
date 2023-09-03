# ✔ Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def tuple_from_path(path_str: str) -> tuple:
    *a, b, c = path_str.replace("\\", ".").split(".")
    path_file = ''
    for i in a:
        path_file = path_file + i + "\\"
    return (path_file, b, c)

path_str = r"D:\new\equipment.txt"
print(tuple_from_path(path_str))