from src.api import send_post_request_to_api


def get_params_to_query_game_rating(sandbox_id):
    params = {
        "operationName": "getProductResult",
        "variables": {"sandboxId": sandbox_id, "locale": "en"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "4a58e53900301bcbfa5a2a576ece55ec1151c0e69cdddb66891ee18c466054ed",
            }
        },
    }

    return params


def to_game_rating(sandbox_id, verbose=True):
    params = get_params_to_query_game_rating(sandbox_id)
    data = send_post_request_to_api(params, verbose=verbose)
    try:
        game_rating = data["data"]["RatingsPolls"]["getProductResult"]
    except (TypeError, KeyError) as e:
        game_rating = None
    return game_rating
