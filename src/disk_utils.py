import json


def save_json(data, filename):
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(data, f)


def load_json(filename):
    with open(filename, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


def get_store_data_fname(iter_no):
    return f'data/store_data_{iter_no}.json'
