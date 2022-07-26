from src.rankings import aggregate_ranking, export_ranking_to_csv
from src.ratings import load_game_ratings
from src.sandboxes import load_sandbox_ids_dict
from src.trim_utils import trim_game_ratings, trim_sandbox_ids_dict


def main():
    sandbox_ids_dict = load_sandbox_ids_dict()
    sandbox_ids_dict = trim_sandbox_ids_dict(sandbox_ids_dict)

    game_ratings = load_game_ratings()
    game_ratings = trim_game_ratings(game_ratings, export_to_json=False)

    ranking = aggregate_ranking(sandbox_ids_dict, game_ratings)
    export_ranking_to_csv(ranking)

    return


if __name__ == "__main__":
    main()
