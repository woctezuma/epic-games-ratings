from src.products import load_slugs_dict
from src.sandboxes import download_sandbox_ids_dict


def main():
    slugs_dict = load_slugs_dict(num_chunks=None)
    products = set(slugs_dict.keys())

    sandbox_ids_dict = download_sandbox_ids_dict(products, verbose=True)

    return


if __name__ == "__main__":
    main()
