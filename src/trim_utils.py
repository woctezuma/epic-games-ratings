from src.disk_utils import save_json, get_trimmed_game_ratings_fname
from src.ratings import is_a_valid_rating


def trim_game_ratings(game_ratings, export_to_json=False):
    trimmed_dict = dict()

    for id, rating in game_ratings.items():
        if is_a_valid_rating(rating):
            trimmed_dict[id] = rating

    if export_to_json:
        save_json(trimmed_dict, get_trimmed_game_ratings_fname())

    return trimmed_dict


def trim_sandbox_ids_dict(sandbox_ids_dict):
    trimmed_dict = dict()

    for slug, sandbox_id in sorted(sandbox_ids_dict.items(), key=lambda x: x[0]):
        if sandbox_id not in trimmed_dict.values():
            s = slug.strip()
            trimmed_dict[s] = sandbox_id

    return trimmed_dict
