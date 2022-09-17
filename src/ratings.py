from src.disk_utils import save_json, get_game_ratings_fname, safe_load_json
from src.query_game_rating import to_game_rating


def has_a_valid_field_value(rating, keyword):
    return bool(keyword in rating and rating[keyword] is not None)


def is_a_valid_rating(rating):
    is_valid = (
        bool(rating is not None)
        and has_a_valid_field_value(rating, "averageRating")
        and has_a_valid_field_value(rating, "ratingCount")
    )

    return is_valid


def download_game_ratings(sandbox_ids, save_every=60, verbose=True):
    game_ratings = load_game_ratings()

    for iter, id in enumerate(sandbox_ids, start=1):
        if id in game_ratings and is_a_valid_rating(game_ratings[id]):
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
    if verbose:
        print(f"Finally saving {iter}/{len(sandbox_ids)}")

    return game_ratings


def load_game_ratings():
    game_ratings = safe_load_json(get_game_ratings_fname())
    return game_ratings
