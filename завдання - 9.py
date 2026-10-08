def get_file_type(extension):
    file_types = {
        ".jpg": "Зображення",
        ".mp3": "Аудіо",
        ".py": "Скрипт Python"
    }

    return file_types.get(extension, "Невідомий формат")

