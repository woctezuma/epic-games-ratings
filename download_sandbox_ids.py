from src.products import load_store_products
from src.sandboxes import download_sandbox_ids_dict


def main():
    num_queries = 4
    products = load_store_products(num_chunks=num_queries)

    sandbox_ids_dict = download_sandbox_ids_dict(products, verbose=True)

    return


if __name__ == "__main__":
    main()
