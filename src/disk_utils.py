import json
import pathlib


def save_json(data, filename, prettify=True):
    with open(filename, "w", encoding="utf8") as f:
        if prettify:
            json.dump(data, f, indent=4)
        else:
            json.dump(data, f)


def load_json(filename):
    with open(filename, "r", encoding="utf8") as f:
        data = json.load(f)
    return data


def safe_load_json(filename):
    try:
        data = load_json(filename)
    except FileNotFoundError:
        data = dict()
    return data


def get_data_folder():
    folder_name = "data"
    pathlib.Path(folder_name).mkdir(exist_ok=True)
    return folder_name


def get_store_data_fname(iter_no):
    folder_name = get_data_folder()
    return f"{folder_name}/store_data_{iter_no}.json"


def get_sandbox_ids_fname():
    folder_name = get_data_folder()
    return f"{folder_name}/sandbox_ids.json"


def get_duplicate_sandbox_ids_fname():
    folder_name = get_data_folder()
    return f"{folder_name}/duplicate_sandbox_ids.json"


def get_game_ratings_fname():
    folder_name = get_data_folder()
    return f"{folder_name}/game_ratings.json"


def get_trimmed_game_ratings_fname():
    folder_name = get_data_folder()
    return f"{folder_name}/trimmed_game_ratings.json"


def get_ranking_fname():
    folder_name = get_data_folder()
    return f"{folder_name}/egs_game_ranking.csv"
