import json


def read_json(file_name: str) -> dict:
    """
    Считывает содержимое json-файла
    :param file_name: путь к файлу
    :return: словарь
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден")
    except IOError:
        raise IOError(f"Ошибка чтения файла")
    except Exception as e:
        raise Exception(f"Ошибка: {str(e)}")


def write_json(file_name: str, text: dict) -> None:
    """
    Записывает данные в json-файл
    :param file_name: путь к файлу
    :param text: данные
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(text, file, ensure_ascii=False, indent=4)
    except IOError:
        raise IOError(f"Ошибка записи в файл")
    except Exception as e:
        raise Exception(f"Ошибка: {str(e)}")


def read_binary_file(file_name: str) -> bytes:
    """
    Считывает содержимое бинарного файла
    :param file_name: путь к файлу
    :return: содержимое файла в бинарном формате
    """
    try:
        with open(file_name, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден")
    except IOError:
        raise IOError(f"Ошибка чтения файла")
    except Exception as e:
        raise Exception(f"Ошибка: {str(e)}")


def write_binary_file(file_name: str, text: bytes) -> None:
    """
    Записывает данные в бинарный файл
    :param file_name: путь к файлу
    :param text: данные для записи
    """
    try:
        with open(file_name, 'wb') as file:
             file.write(text)
    except IOError:
        raise IOError(f"Ошибка записи в файл")
    except Exception as e:
         raise Exception(f"Ошибка: {str(e)}")
