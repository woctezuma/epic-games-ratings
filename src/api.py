import requests


def get_graphql_api_url(subdomain="graphql"):
    return f"https://{subdomain}.epicgames.com/graphql"


def get_store_api_url():
    return get_graphql_api_url(subdomain="store")


def send_get_to_api(params, subdomain="graphql", verbose=True):
    r = requests.get(get_graphql_api_url(subdomain=subdomain), params=params)
    return to_data(r, verbose=verbose)


def send_post_to_api(json_data, subdomain="graphql", verbose=True):
    r = requests.post(get_graphql_api_url(subdomain=subdomain), json=json_data)
    return to_data(r, verbose=verbose)


def to_data(response, verbose=True):
    if response.ok:
        data = response.json()
    else:
        data = None
        if verbose:
            print(f"Status code = {response.status_code}")
    return data
