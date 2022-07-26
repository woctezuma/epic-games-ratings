from src.cursor_utils import compute_cursor, compute_num_queries
from src.disk_utils import save_json, load_json, get_store_data_fname
from src.query_store_data import to_store_data


def download_store_data(use_preset_operation=False, verbose=True):
    iter_no = 0
    store_data = to_store_data(
        cursor=compute_cursor(iter_no),
        use_preset_operation=use_preset_operation,
        verbose=verbose,
    )
    save_json(store_data, get_store_data_fname(iter_no))

    num_queries = compute_num_queries(store_data)
    print(f"#queries: {num_queries}")

    for iter_no in range(1, num_queries):
        store_data = to_store_data(
            cursor=compute_cursor(iter_no),
            use_preset_operation=use_preset_operation,
            verbose=verbose,
        )
        save_json(store_data, get_store_data_fname(iter_no))

    return num_queries


def load_slugs_dict(num_chunks, keyword="pageSlug", verbose=True):
    slugs_dict = dict()

    for chunk_no in range(num_chunks):
        store_data = load_json(get_store_data_fname(chunk_no))
        for e in store_data["elements"]:
            title = e["title"]
            offer_mapping = e["offerMappings"]
            namespace_mapping = e["catalogNs"]["mappings"]

            mappings = []
            if offer_mapping is not None:
                mappings += offer_mapping
            if namespace_mapping is not None:
                mappings += namespace_mapping

            for p in mappings:
                try:
                    slug = p[keyword]
                except KeyError:
                    continue

                if slug in slugs_dict:
                    slugs_dict[slug].add(title)
                else:
                    slugs_dict[slug] = {title}

    if verbose:
        print(f"#{keyword}s = {len(slugs_dict)}")

    return slugs_dict
