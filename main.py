from os import listdir, system
from os.path import join

import extractor
import organizer
from archiver import archiver
from delete_credits import delete_credit


def my_print(text: str) -> None:
    print(".".center(50, "."))
    print()
    print(text.center(50, "~"))


def main():
    working_dir = organizer.get_working_directory()
    if not working_dir:
        print("Cancelling...".center(50, "-"))
        return

    items = organizer.check_current_dir(working_dir)
    organizer.organize_files(items)
    my_print("MAIN")

    for path in organizer.get_folders_path(working_dir):
        for file_or_folder in listdir(path):
            file_folder_dir = join(path, file_or_folder).replace("/", "\\")
            if extractor.check_extension(file_folder_dir):
                my_print(f"EXTRACTING >>> {file_or_folder}")
                system(extractor.extract_archive_command(file_folder_dir, file_or_folder))
                my_print(f"DELETING >>> {file_or_folder}")
                system(extractor.delete_archive_command(file_folder_dir))
                my_print("-".center(50, "-"))

    my_print("Deleting Credits")
    delete_credit(working_dir)

    my_print("Archiving")
    archiver(working_dir)


if __name__ == "__main__":
    main()
