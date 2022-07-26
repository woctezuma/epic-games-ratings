def compute_prior(game_ratings, verbose=True):
    num_games = len(game_ratings)
    sum_rating = sum(r["averageRating"] for r in game_ratings.values())
    sum_count = sum(r["ratingCount"] for r in game_ratings.values())

    prior = {
        "averageRating": sum_rating / num_games,
        "ratingCount": sum_count / num_games,
    }

    if verbose:
        print(f'Prior {prior["averageRating"]:.2f} ({prior["ratingCount"]:.0f} votes)')

    return prior


def compute_bayes_rating(rating, prior):
    numerator = (
        rating["ratingCount"] * rating["averageRating"]
        + prior["ratingCount"] * prior["averageRating"]
    )
    denominator = rating["ratingCount"] + prior["ratingCount"]
    return numerator / denominator
