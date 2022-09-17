from src.disk_utils import get_duplicate_sandbox_ids_fname
from src.disk_utils import save_json, get_sandbox_ids_fname, safe_load_json
from src.query_sandbox_id import to_sandbox_id


def is_a_valid_sandbox_id(sandbox_id):
    is_valid = bool(sandbox_id is not None)

    return is_valid


def download_sandbox_ids_dict(slugs, save_every=60, verbose=True):
    sandbox_ids_dict = load_sandbox_ids_dict()
    duplicate_sandbox_ids_dict = load_duplicate_sandbox_ids_dict()

    slugs = sorted(slugs, key=lambda x: (len(x), x))
    for iter, s in enumerate(slugs, start=1):
        if s in sandbox_ids_dict and is_a_valid_sandbox_id(sandbox_ids_dict[s]):
            continue
        if s in duplicate_sandbox_ids_dict:
            continue

        id = to_sandbox_id(s, verbose=verbose)

        if verbose and id is not None:
            print(f"{s} -> {id}")

        if id not in sandbox_ids_dict.values() or s in sandbox_ids_dict:
            sandbox_ids_dict[s] = id
        else:
            duplicate_sandbox_ids_dict[s] = id

        if iter % save_every == 0:
            save_json(sandbox_ids_dict, get_sandbox_ids_fname())
            save_json(duplicate_sandbox_ids_dict, get_duplicate_sandbox_ids_fname())
            if verbose:
                print(f"Saving {iter}/{len(slugs)}")

    save_json(sandbox_ids_dict, get_sandbox_ids_fname())
    save_json(duplicate_sandbox_ids_dict, get_duplicate_sandbox_ids_fname())
    if verbose:
        print(f"Finally saving {iter}/{len(slugs)}")

    return sandbox_ids_dict


def load_sandbox_ids_dict():
    sandbox_ids_dict = safe_load_json(get_sandbox_ids_fname())
    return sandbox_ids_dict


def load_duplicate_sandbox_ids_dict():
    sandbox_ids_dict = safe_load_json(get_duplicate_sandbox_ids_fname())
    return sandbox_ids_dict
