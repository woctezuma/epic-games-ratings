from src.ratings import download_game_ratings
from src.sandboxes import load_sandbox_ids


def main():
    sandbox_ids = load_sandbox_ids()

    game_ratings = download_game_ratings(sandbox_ids, verbose=True)

    return


if __name__ == "__main__":
    main()
