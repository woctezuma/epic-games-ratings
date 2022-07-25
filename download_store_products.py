from src.products import download_store_data, load_store_products


def main():
    num_queries = download_store_data()
    products = load_store_products(num_chunks=num_queries)
    return


if __name__ == "__main__":
    main()
