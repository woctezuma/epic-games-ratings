from src.query_sandbox_id import to_sandbox_id


def download_sandbox_ids_based_on_products(products, verbose=True):
    slugs = set(products.values())

    if verbose:
        print(f'#unique slugs = {len(slugs)}')

    sandbox_ids = download_sandbox_ids_based_on_slugs(slugs)

    return sandbox_ids


def download_sandbox_ids_based_on_slugs(slugs, verbose=True):
    sandbox_ids = dict()

    for s in slugs:
        id = to_sandbox_id(s)

        if verbose and id is not None:
            print(f'{s} -> {id}')

        sandbox_ids[s] = to_sandbox_id(s)

    return sandbox_ids
