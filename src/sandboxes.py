from src.disk_utils import save_json, get_sandbox_ids_fname, load_json
from src.query_sandbox_id import to_sandbox_id


def download_sandbox_ids(slugs, save_every=60, verbose=True):
    try:
        sandbox_ids = load_json(get_sandbox_ids_fname())
    except FileNotFoundError:
        sandbox_ids = dict()

    for iter, s in enumerate(slugs, start=1):
        id = to_sandbox_id(s, verbose=verbose)

        if verbose and id is not None:
            print(f"{s} -> {id}")

        sandbox_ids[s] = id

        if iter % save_every == 0:
            save_json(sandbox_ids, get_sandbox_ids_fname())

    save_json(sandbox_ids, get_sandbox_ids_fname())

    return sandbox_ids
