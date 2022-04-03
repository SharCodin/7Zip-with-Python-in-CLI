import os
from timeit import default_timer as Timer


def delete_credit(working_dir: str):
    startTimer = Timer()
    nameList = [
        "girlcelly@[Anime-sharing.com].txt",
        "H-Game uploaded by baka girlcelly - NemuAndHaruka.txt",
        "NemuAndHaruka.png",
        "Game uploaded by baka girlcelly - NemuAndHaruka.txt",
        "OTOMI",
        "OTOMI-GAMES.COM.url",
        "WWW.OVAGAMES.COM.url",
        "codex.nfo"
    ]
    top: str = working_dir
    number_of_files_deleted = 0
    for dirpaths, _, filenames in os.walk(top):
        for fname in filenames:
            if fname in nameList:
                file2remove = os.path.join(dirpaths, fname)
                os.remove(file2remove)
                number_of_files_deleted += 1
    stopTimer = Timer()
    print("Number of files deleted: " + str(number_of_files_deleted))
    print("Total time: " + (str(round(stopTimer - startTimer, 2))))
    print("-" * 20)
