from src.products import load_store_products
from src.sandboxes import download_sandbox_ids_based_on_products


def main():
    num_queries = 4
    products = load_store_products(num_chunks=num_queries)

    sandbox_ids = download_sandbox_ids_based_on_products(products, verbose=True)

    return


if __name__ == "__main__":
    main()
