def compute_prior(game_ratings):
    num_games = len(game_ratings)
    sum_rating = sum(r["averageRating"] for r in game_ratings.values())
    sum_count = sum(r["ratingCount"] for r in game_ratings.values())

    prior = {
        "averageRating": sum_rating / num_games,
        "ratingCount": sum_count / num_games,
    }

    return prior


def compute_bayes_rating(rating, prior):
    numerator = (
        rating["ratingCount"] * rating["averageRating"]
        + prior["ratingCount"] * prior["averageRating"]
    )
    denominator = rating["ratingCount"] + prior["ratingCount"]
    return numerator / denominator
