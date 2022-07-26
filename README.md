# Epic Games Ratings

This repository contains Python code to data-mine ratings at the Epic Games Store (EGS).

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

## References

- [`nikop/epic-games-ratings`][madjoki-egs-ratings]
- [`ToutinRoger/EpicGraphQL`][egs-api-graphql]
- [`woctezuma/Steam-Bayesian-Average`][Steam-Bayesian-Average]
- Bayesian average [on Wikipedia][bayes-wiki]
- Paul Masurel, [Of Bayesian average and star ratings][bayes-fulmicoton], March 2013

<!-- Definitions -->

[madjoki-egs-ratings]: <https://github.com/nikop/epic-games-ratings>
[egs-api-graphql]: <https://github.com/ToutinRoger/EpicGraphQL>
[bayes-wiki]: <https://en.wikipedia.org/wiki/Bayesian_average>
[bayes-fulmicoton]: <https://fulmicoton.com/posts/bayesian_rating/>
[Steam-Bayesian-Average]: <https://github.com/woctezuma/Steam-Bayesian-Average>
[colab-notebook]: <https://colab.research.google.com/github/woctezuma/epic-games-ratings/blob/colab/epic-games-ratings.ipynb>
[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
[ranking-url]: <https://gist.github.com/woctezuma/4f284efaac738d4f2714dcf83053747f>

