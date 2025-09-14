#№89 - создание программы для работы с музыкальными файлами,
# позволяющая воспроизводить и сохранять файлы с обработкой исключений
import pygame  #обязательно для работы с мультимедиа
import shutil #для операций с файлами
import os #для работы с операционкой

#инициализация аудиосистемы для работы со звуком, init() - запускает аудиосистему
pygame.mixer.init()


#функция воспроизведения музыкального файла
def play_music(file_path):  #принимает путь к музыкальному файлу
    try:
        if not os.path.exists(file_path): #проверка на наличие файла
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        pygame.mixer.music.load(file_path) #загрузка аудиофайла в аудиоплеер
        pygame.mixer.music.play()  #запуск аудиофайла
        print(f"Воспроизведение: {file_path}")

        #ожидаем завершения воспроизведения
        while pygame.mixer.music.get_busy(): #get_busy() возвращает True, когда музыка проиграла
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Ошибка при воспроизведении: {e}")


#функция сохранения (копирования) музыкального файла
def save_music(source_path, destination_path): #принимает изначальное место и место сохранения
    try:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Исходный файл не найден: {source_path}")

        shutil.copy(source_path, destination_path)
        print(f"Файл сохранён в: {destination_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


