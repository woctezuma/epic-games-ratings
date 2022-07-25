from src.disk_utils import save_json, get_sandbox_ids_fname
from src.query_sandbox_id import to_sandbox_id


def download_sandbox_ids(slugs, verbose=True):
    sandbox_ids = dict()

    for s in slugs:
        id = to_sandbox_id(s, verbose=verbose)

        if verbose and id is not None:
            print(f"{s} -> {id}")

        sandbox_ids[s] = id

    save_json(sandbox_ids, get_sandbox_ids_fname())

    return sandbox_ids
