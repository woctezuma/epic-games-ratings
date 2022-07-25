import requests


def get_graphql_api_url():
    return "https://graphql.epicgames.com/graphql"


def send_get_to_api(params, verbose=True):
    r = requests.get(get_graphql_api_url(), params=params)
    return to_data(r, verbose=verbose)


def send_post_to_api(json_data, verbose=True):
    r = requests.post(get_graphql_api_url(), json=json_data)
    return to_data(r, verbose=verbose)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
