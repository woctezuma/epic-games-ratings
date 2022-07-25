from src.ratings import download_game_ratings
from src.sandboxes import load_sandbox_ids_dict


def main():
    sandbox_dict = load_sandbox_ids_dict()
    sandbox_ids = set(sandbox_dict.values())

    game_ratings = download_game_ratings(sandbox_ids, verbose=True)

    return


if __name__ == "__main__":
    main()
