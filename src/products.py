from src.cursor_utils import compute_cursor, compute_num_queries
from src.disk_utils import save_json, load_json, get_store_data_fname
from src.query_store_data import to_store_data


def download_store_data():
    iter_no = 0
    store_data = to_store_data(cursor=compute_cursor(iter_no))
    save_json(store_data, get_store_data_fname(iter_no))

    num_queries = compute_num_queries(store_data)
    print(f"#queries: {num_queries}")

    for iter_no in range(1, num_queries):
        store_data = to_store_data(cursor=compute_cursor(iter_no))
        save_json(store_data, get_store_data_fname(iter_no))

    return num_queries


def load_store_products(num_chunks, verbose=True):
    products = dict()

    for chunk_no in range(num_chunks):
        store_data = load_json(get_store_data_fname(chunk_no))
        for e in store_data["elements"]:
            title = e["title"]
            slug = e["urlSlug"]
            products[title] = slug

    if verbose:
        print(f"#products = {len(products)}")

    return products
