from src.products import load_slugs_dict
from src.sandboxes import download_sandbox_ids_dict


def main():
    num_queries = 4
    slugs_dict = load_slugs_dict(num_chunks=num_queries)
    products = set(slugs_dict.keys())

    sandbox_ids_dict = download_sandbox_ids_dict(products, verbose=True)

    return


if __name__ == "__main__":
    main()
