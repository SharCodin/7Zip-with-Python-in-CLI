import os
from shutil import move
from tkinter import Tk
from tkinter.filedialog import askdirectory


def get_working_directory() -> str:
    """Ask user for the working directory. This must be a root directory not sub-directory"""
    root = Tk()
    root.attributes("-topmost", True)
    working_directory = askdirectory(initialdir=os.getcwd())
    root.destroy()
    return working_directory


def check_current_dir(dir_path: str) -> list[str]:
    """Check if working directory contains files"""
    files: list[str] = []
    for item in os.listdir(dir_path):
        full_path = os.path.join(dir_path, item)
        if os.path.isfile(full_path):
            files.append(full_path.replace("/", "\\"))
    return files


def organize_files(items: list[str]) -> None:
    """Check for files and move them to their folders."""
    print("Organizing Files".center(50, "-"))
    for file in items:
        file_ext = os.path.split(file)
        file_name = os.path.splitext(file_ext[1])
        print(f"{file_name}")
        file_destination = os.path.join(file_ext[0], file_name[0])
        os.makedirs(file_destination)
        move(file, file_destination)


def get_folders_path(working_dir: str) -> list[str]:
    folder_path: list[str] = []
    for folder in os.listdir(working_dir):
        folder_path.append(os.path.join(working_dir, folder))
    return folder_path
