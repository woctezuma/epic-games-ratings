from src.disk_utils import save_json, get_sandbox_ids_fname, load_json
from src.query_sandbox_id import to_sandbox_id


def download_sandbox_ids(slugs, save_every=60, verbose=True):
    sandbox_ids = load_sandbox_ids()

    for iter, s in enumerate(slugs, start=1):
        if s in sandbox_ids and sandbox_ids[s] is not None:
            continue

        id = to_sandbox_id(s, verbose=verbose)

        if verbose and id is not None:
            print(f"{s} -> {id}")

        sandbox_ids[s] = id

        if iter % save_every == 0:
            save_json(sandbox_ids, get_sandbox_ids_fname())

    save_json(sandbox_ids, get_sandbox_ids_fname())

    return sandbox_ids


def load_sandbox_ids():
    try:
        sandbox_ids = load_json(get_sandbox_ids_fname())
    except FileNotFoundError:
        sandbox_ids = dict()
    return sandbox_ids
