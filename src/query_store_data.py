from src.api import send_post_request_to_api

from src.cursor_utils import get_num_games_per_query


def get_params_to_query_store_data(cursor):
    step = get_num_games_per_query()

    params = {
        "operationName": "searchStoreQuery",
        "variables": {
            "category": "games",
            "country": "FR",
            "start": cursor,
            "count": step,
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "13a2b6787f1a20d05c75c54c78b1b8ac7c8bf4efc394edf7a5998fdf35d1adb0",
            }
        },
    }

    return params


def get_json_data_to_query_store_data(cursor, include_dlc=False, verbose=True):
    step = get_num_games_per_query()

    if include_dlc:
        category_str = ""
    else:
        category_str = 'category: "games", '

    prefix = "{Catalog {searchStore"
    param_str = f"({category_str}start: {cursor}, count: {step})"
    slug_str = 'productSlug offerMappings {pageSlug} catalogNs {mappings(pageType: "productHome") {pageSlug}}'
    content_str = "{ paging {count total} elements {title urlSlug " + slug_str + " } }"
    suffix = "}}"

    query = prefix + param_str + content_str + suffix

    if verbose:
        print(f"Query: {query}")

    json_data = {"query": query}

    return json_data


def to_store_data(cursor, use_preset_operation=False, include_dlc=False, verbose=True):
    if use_preset_operation:
        params = get_params_to_query_store_data(cursor)
        data = send_post_request_to_api(params, verbose=verbose)
    else:
        json_data = get_json_data_to_query_store_data(
            cursor, include_dlc=include_dlc, verbose=verbose
        )
        data = send_post_request_to_api(json_data, verbose=verbose)

    store_data = data["data"]["Catalog"]["searchStore"]

    return store_data
