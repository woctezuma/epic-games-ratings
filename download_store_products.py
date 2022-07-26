from src.products import download_store_data, load_slugs_dict


def main():
    num_queries = download_store_data(use_preset_operation=False, verbose=True)
    slugs_dict = load_slugs_dict(num_chunks=num_queries)
    return


if __name__ == "__main__":
    main()
