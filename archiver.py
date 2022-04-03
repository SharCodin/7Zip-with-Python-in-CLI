import os


def archiver(working_dir: str):
    print(f"Please make sure you do not have UNWANTED FILES or folders in this directory: \n{working_dir}.\n")

    ext = input("\n\nExtension: ").lower()

    if ext=="" or ext=="zip":
        ext='zip'
    elif ext=="cbr":
        pass
    else:
        print("Exiting...")
        return

    command_list: list[dict[int, str]] = []
    for index, folder in enumerate(os.listdir(working_dir)):
        folder_path = os.path.join(working_dir, folder)
        zip_path = f"{folder_path}\\{folder}.{ext}"
        if len(zip_path) > 200:
            short_folder_name = str(folder.split(" ")[0]) + "~"
            zip_path = f"{folder_path}\\{short_folder_name}.{ext}"
        zip_command = None
        if ext=='zip':
            zip_command = f'7z a -mx0 -v2040m -sdel "{zip_path}" "{folder_path}" && echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="'
        if ext=='cbr':
            zip_command = f'7z a -mx0 -sdel "{zip_path}" "{folder_path}" && echo "=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="'
        command_list.append({index: zip_command})
        print(index, folder)

    prompt = input("\nPlease check the above list. \n\nA - All\nC - Choose\nN - Exit\n\nChoose: ")

    if prompt.lower() == "c":
        choices = input("Which numbers (separate with space): ")
        choices_list = choices.split()
        commands: list[str] = []
        for command_dict in command_list:
            for key, value in command_dict.items():
                if str(key) in choices_list:
                    commands.append(value)
        command = " && ".join(commands)
        os.system(command)
    elif prompt.lower() == "a":
        commands = []
        for command_dict in command_list:
            for _, value in command_dict.items():
                commands.append(value)
        command = " && ".join(commands)
        os.system(command)
    else:
        print("Exiting...")
        return
