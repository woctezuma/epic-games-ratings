from src.disk_utils import save_json, get_game_ratings_fname, load_json
from src.query_game_rating import to_game_rating


def download_game_ratings(sandbox_ids, save_every=60, verbose=True):
    game_ratings = load_game_ratings()

    for iter, id in enumerate(sandbox_ids, start=1):
        if id in game_ratings and game_ratings[id] is not None:
            continue

        rating = to_game_rating(id, verbose=verbose)

        if verbose and rating is not None:
            print(f"{id} -> {rating}")

        game_ratings[id] = rating

        if iter % save_every == 0:
            save_json(game_ratings, get_game_ratings_fname())
            if verbose:
                print(f"Saving {iter}/{len(sandbox_ids)}")

    save_json(game_ratings, get_game_ratings_fname())

    return game_ratings


def load_game_ratings():
    try:
        game_ratings = load_json(get_game_ratings_fname())
    except FileNotFoundError:
        game_ratings = dict()
    return game_ratings
