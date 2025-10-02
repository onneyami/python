import os
import shutil
import pygame
import argparse
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

# Initialize audio system
pygame.mixer.init()

# Play music file
def play_music(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")
    except Exception as e:
        messagebox.showerror("Playback error", str(e))

# Save music file
def save_music(source_path, destination_path):
    try:
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {source_path}")
        shutil.copy(source_path, destination_path)
        print(f"File saved to: {destination_path}")
    except Exception as e:
        messagebox.showerror("Save error", str(e))

# Get track duration
def get_track_length(file_path):
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound.get_length()
    except Exception:
        return 0

# Load and scale icon
def load_icon(path, size=(24, 24)):
    try:
        img = Image.open(path)
        img = img.resize(size, Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# Create graphical interface
def create_gui():
    try:
        from tkinterdnd2 import TkinterDnD, DND_FILES
        window = TkinterDnD.Tk()
        drag_enabled = True
    except ImportError:
        window = tk.Tk()
        drag_enabled = False
        print("Drag-and-drop not available: tkinterdnd2 not installed")

    window.title("Music Player 🎵")
    window.geometry("700x500")
    window.configure(bg="#f0f0f0")

    # Progress bar
    progress = tk.DoubleVar()
    progress_bar = ttk.Progressbar(window, variable=progress, maximum=100, length=500)
    progress_bar.pack(pady=20)

    # Update progress
    def update_progress_bar(duration):
        if pygame.mixer.music.get_busy():
            current_pos = pygame.mixer.music.get_pos() / 1000  # milliseconds → seconds
            if duration > 0:
                progress.set((current_pos / duration) * 100)
            window.after(500, lambda: update_progress_bar(duration))
        else:
            progress.set(0)

    # Play file
    def choose_file_to_play():
        file_path = filedialog.askopenfilename(title="Select music file")
        if file_path:
            play_music(file_path)
            duration = get_track_length(file_path)
            progress.set(0)
            update_progress_bar(duration)

    # Save file
    def choose_file_to_save():
        source_path = filedialog.askopenfilename(title="Select source file")
        if source_path:
            destination_path = filedialog.asksaveasfilename(title="Select save location")
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

    # Load icons
    play_icon = load_icon("content/play_icon.png")
    save_icon = load_icon("content/save_icon.png")
    exit_icon = load_icon("content/exit_icon.png")

    # Buttons
    play_button = tk.Button(window, text="▶ Play", image=play_icon, compound="left",
                            command=choose_file_to_play, padx=10, pady=5)
    play_button.pack(pady=10)

    save_button = tk.Button(window, text="💾 Save", image=save_icon, compound="left",
                            command=choose_file_to_save, padx=10, pady=5)
    save_button.pack(pady=10)

    exit_button = tk.Button(window, text="❌ Exit", image=exit_icon, compound="left",
                            command=window.quit, padx=10, pady=5)
    exit_button.pack(pady=10)

    # Enable drag-and-drop
    if drag_enabled:
        window.drop_target_register(DND_FILES)
        window.dnd_bind('<<Drop>>', drop)

    window.mainloop()

# Main function
def main():
    parser = argparse.ArgumentParser(description="Music file utility")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    play_parser = subparsers.add_parser("play", help="Play music file")
    play_parser.add_argument("file", help="Path to music file")

    save_parser = subparsers.add_parser("save", help="Save music file")
    save_parser.add_argument("source", help="Source file path")
    save_parser.add_argument("destination", help="Destination file path")

    gui_parser = subparsers.add_parser("gui", help="Launch graphical interface")

    args = parser.parse_args()

    if args.command == "play":
        play_music(args.file)
    elif args.command == "save":
        save_music(args.source, args.destination)
    elif args.command == "gui" or args.command is None:
        create_gui()
    else:
        parser.print_help()

# Entry point
if __name__ == "__main__":
    main()
