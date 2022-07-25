from src.api import send_get_to_api


def get_params_to_query_sandbox_id(page_slug):
    params = {
        "operationName": "getMappingByPageSlug",
        "variables": {"pageSlug": page_slug, "locale": "en"},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "781fd69ec8116125fa8dc245c0838198cdf5283e31647d08dfa27f45ee8b1f30",
            }
        },
    }

    return params


def to_sandbox_id(page_slug, verbose=True):
    params = get_params_to_query_sandbox_id(page_slug)
    data = send_get_to_api(params, subdomain="store", verbose=verbose)
    try:
        sandbox_id = data["data"]["StorePageMapping"]["mapping"]["sandboxId"]
    except TypeError:
        sandbox_id = None
    return sandbox_id
