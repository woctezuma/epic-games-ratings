from src.bayes_ratings import compute_prior, compute_bayes_rating
from src.disk_utils import get_ranking_fname


def aggregate_ranking(sandbox_ids_dict, game_ratings):
    ranking = list()

    prior = compute_prior(game_ratings)

    for slug, sandbox_id in sandbox_ids_dict.items():
        try:
            rating = game_ratings[sandbox_id]
        except KeyError:
            continue

        ranking.append(
            {
                "slug": slug,
                "id": sandbox_id,
                "rating": rating["averageRating"],
                "count": rating["ratingCount"],
                "bayes_rating": compute_bayes_rating(rating, prior),
            }
        )

    return ranking


def sort_ranking(ranking):
    return sorted(ranking, key=lambda x: x["bayes_rating"], reverse=True)


def export_ranking_to_csv(ranking):
    with open(get_ranking_fname(), "w", encoding="utf8") as f:
        f.write("Game slug,Epic Games rating,Number of raters, Bayes rating\n")
        for entry in sort_ranking(ranking):
            f.write(
                f"{entry['slug']},{entry['rating']:.2f},{entry['count']},{entry['bayes_rating']:.2f}\n"
            )

    return
