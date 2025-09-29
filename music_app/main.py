import os
import shutil
import pygame
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

# Инициализация аудиосистемы
pygame.mixer.init()

# Воспроизведение музыкального файла
def play_music(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Воспроизведение: {file_path}")
    except Exception as e:
        messagebox.showerror("Ошибка воспроизведения", str(e))

# Сохранение музыкального файла
def save_music(source_path, destination_path):
    try:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Исходный файл не найден: {source_path}")
        shutil.copy(source_path, destination_path)
        print(f"Файл сохранён в: {destination_path}")
    except Exception as e:
        messagebox.showerror("Ошибка сохранения", str(e))

# Получение длительности трека
def get_track_length(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound.get_length()
    except Exception:
        return 0

# Загрузка иконки с масштабированием
def load_icon(path, size=(24, 24)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# Создание графического интерфейса
def create_gui():
    try:
        from tkinterdnd2 import TkinterDnD, DND_FILES
        window = TkinterDnD.Tk()
        drag_enabled = True
    except ImportError:
        window = tk.Tk()
        drag_enabled = False
        print("Drag-and-drop не доступен: tkinterdnd2 не установлен")

    window.title("Музыкальный плеер 🎵")
    window.geometry("700x500")
    window.configure(bg="#f0f0f0")

    # Прогресс-бар
    progress = tk.DoubleVar()
    progress_bar = ttk.Progressbar(window, variable=progress, maximum=100, length=500)
    progress_bar.pack(pady=20)

    # Обновление прогресса
    def update_progress_bar(duration):
        if pygame.mixer.music.get_busy():
            current_pos = pygame.mixer.music.get_pos() / 1000  # миллисекунды → секунды
            if duration > 0:
                progress.set((current_pos / duration) * 100)
            window.after(500, lambda: update_progress_bar(duration))
        else:
            progress.set(0)

    # Воспроизведение файла
    def choose_file_to_play():
        file_path = filedialog.askopenfilename(title="Выберите музыкальный файл")
        if file_path:
            play_music(file_path)
            duration = get_track_length(file_path)
            progress.set(0)
            update_progress_bar(duration)

    # Сохранение файла
    def choose_file_to_save():
        source_path = filedialog.askopenfilename(title="Выберите исходный файл")
        if source_path:
            destination_path = filedialog.asksaveasfilename(title="Выберите место сохранения")
            if destination_path:
                save_music(source_path, destination_path)

    # Drag-and-drop
    def drop(event):
        file_path = event.data.strip()
        if os.path.isfile(file_path):
            play_music(file_path)
            duration = get_track_length(file_path)
            progress.set(0)
            update_progress_bar(duration)

    # Загрузка иконок
    play_icon = load_icon("content/play_icon.png")
    save_icon = load_icon("content/save_icon.png")
    exit_icon = load_icon("content/exit_icon.png")

    # Кнопки
    play_button = tk.Button(window, text="▶ Воспроизвести", image=play_icon, compound="left",
                            command=choose_file_to_play, padx=10, pady=5)
    play_button.pack(pady=10)

    save_button = tk.Button(window, text="💾 Сохранить", image=save_icon, compound="left",
                            command=choose_file_to_save, padx=10, pady=5)
    save_button.pack(pady=10)

    exit_button = tk.Button(window, text="❌ Выход", image=exit_icon, compound="left",
                            command=window.quit, padx=10, pady=5)
    exit_button.pack(pady=10)

    # Активация drag-and-drop
    if drag_enabled:
        window.drop_target_register(DND_FILES)
        window.dnd_bind('<<Drop>>', drop)

    window.mainloop()

# Основная функция
def main():
    parser = argparse.ArgumentParser(description="Программа для работы с музыкальными файлами")
    subparsers = parser.add_subparsers(dest="command", help="Команды")

    play_parser = subparsers.add_parser("play", help="Воспроизвести музыкальный файл")
    play_parser.add_argument("file", help="Путь к музыкальному файлу")

    save_parser = subparsers.add_parser("save", help="Сохранить музыкальный файл")
    save_parser.add_argument("source", help="Исходный путь к файлу")
    save_parser.add_argument("destination", help="Путь для сохранения файла")

    gui_parser = subparsers.add_parser("gui", help="Запустить графический интерфейс")

    args = parser.parse_args()

    if args.command == "play":
        play_music(args.file)
    elif args.command == "save":
        save_music(args.source, args.destination)
    elif args.command == "gui" or args.command is None:
        create_gui()
    else:
        parser.print_help()

# Запуск
if __name__ == "__main__":
    main()
