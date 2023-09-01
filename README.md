# Epic Games Ratings

[![Code Quality][codacy-image]][codacy]

This repository contains Python code to data-mine ratings at the Epic Games Store (EGS).

![Ranking of games based on the Bayesian average rating][img-cover]

## Disclaimer

The leak has been plugged, so the code cannot fetch `ratingCount` directly from Epic Games anymore.

> **Note**
> As of December 15, 2022, the official ranking seems to be using Bayesian average ratings! 🥳🎉
> 
> For comparison:
> - [the latest unofficial ranking][unofficial-ranking-latest], on September 24, 2022,
> - [the official ranking][official-ranking-new-sorting-order], on December 15, 2022.

> **Note**
> Unfortunately, the official ranking was reverted back to using **raw** ratings later on the same day.

> **Note**
> As of August 31, 2023, the official ranking uses a mysterious sorting order! 😱
>
> For investigation:
> - [the official ranking][official-ranking-mysterious-sorting-order-August-31-2023], on August 31, 2023,
> - [the official ranking][official-ranking-mysterious-sorting-order-September-01-2023], on September 1, 2023.

## Requirements

-   Install the latest version of [Python 3.X][python-download-url].
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To retrieve the `pageSlug` for every store product, run:
```bash
python download_store_products.py
```
Caveat: different store products can be associated with the same `pageSlug`, despite having different `title` values.

To retrieve the `sandboxId` associated with every `pageSlug`, run:
```bash
python download_sandbox_ids.py
```

To retrieve the ratings associated with every `sandboxId`, run:
```bash
python download_game_ratings.py
```

To export trimmed results to JSON and CSV, run:
```bash
python export_results.py
```

Alternatively:

-   Run [`epic-games-ratings.ipynb`][colab-notebook]
[![Open In Colab][colab-badge]][colab-notebook]

## Results

A ranking of games sorted by Bayesian average rating is available [here][ranking-url].

NB: the ranking does not feature [delisted games][delisted-games].

## References

- Official ranking of [*Top Player Reviewed PC Titles*][egs-official-ranking], computed by Epic Games
- [`nikop/epic-games-ratings`][madjoki-egs-ratings]
- [`woctezuma/epic-games-achievements`][epic-games-achievements]
- [`woctezuma/epic-games-player-estimates`][epic-games-player-estimates]
- [`ToutinRoger/EpicGraphQL`][egs-api-graphql]
- [`woctezuma/Steam-Bayesian-Average`][Steam-Bayesian-Average]
- Bayesian average [on Wikipedia][bayes-wiki]
- Paul Masurel, [Of Bayesian average and star ratings][bayes-fulmicoton], March 2013

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/epic-games-ratings/wiki/img/cover.png>
[codacy]: <https://www.codacy.com/gh/woctezuma/epic-games-ratings>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/0e6fdef52e3e4f7b917b42ad49e7ff06>
[python-download-url]: <https://www.python.org/downloads/>
[delisted-games]: <https://github.com/woctezuma/epic-games-ratings/wiki/Delisted-Games>
[madjoki-egs-ratings]: <https://github.com/nikop/epic-games-ratings>
[epic-games-achievements]: <https://github.com/woctezuma/epic-games-achievements>
[epic-games-player-estimates]: <https://github.com/woctezuma/epic-games-player-estimates>
[egs-api-graphql]: <https://github.com/ToutinRoger/EpicGraphQL>
[bayes-wiki]: <https://en.wikipedia.org/wiki/Bayesian_average>
[bayes-fulmicoton]: <https://fulmicoton.com/posts/bayesian_rating/>
[Steam-Bayesian-Average]: <https://github.com/woctezuma/Steam-Bayesian-Average>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-ratings/blob/colab/epic-games-ratings.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[ranking-url]: <data/egs_game_ranking.csv>
[egs-official-ranking]: <https://store.epicgames.com/collection/top-player-reviewed>
[unofficial-ranking-latest]: <https://github.com/woctezuma/epic-games-ratings/wiki/Ranking-(2022-09-24)>
[official-ranking-new-sorting-order]: <https://github.com/woctezuma/epic-games-ratings/wiki/Official-Ranking-(2022-12-15)>
[official-ranking-mysterious-sorting-order-August-31-2023]: <https://github.com/woctezuma/epic-games-ratings/wiki/Official-Ranking-(2023-08-31)>
[official-ranking-mysterious-sorting-order-September-01-2023]: <https://github.com/woctezuma/epic-games-ratings/wiki/Official-Ranking-(2023-09-01)>
