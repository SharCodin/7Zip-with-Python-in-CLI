from os import chdir
from os.path import isfile, split, splitext


def check_extension(path: str) -> bool:
    if not isfile(path):
        return False

    valid_ext: list[str] = [".zip", ".rar"]
    invalid_parts = [f"part{x}".zfill(2) for x in range(2, 101)]
    if splitext(path)[1] in valid_ext:
        for part in invalid_parts:
            if part not in path:
                return True
    return False


def extract_archive_command(src_path: str, file_name: str) -> str:
    chdir(split(src_path)[0])
    folder = splitext(file_name)[0]
    return f'7z x "{src_path}" -o"{folder}" -y'


def delete_archive_command(src_path: str) -> str:
    return f'del "{src_path}"'


def archive_folder_command(src_path: str) -> str:
    dst_path: str = split(src_path)[0]
    return f'7z a -mx0 -v2040m -sdel "{dst_path}\\compressed.zip" "{dst_path}"'
