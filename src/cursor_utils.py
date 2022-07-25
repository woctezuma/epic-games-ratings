def get_num_games_per_query():
    return 1000


def compute_cursor(iter_no):
    return iter_no * get_num_games_per_query()


def extract_num_games(store_data):
    return store_data["paging"]["total"]


def compute_num_queries(store_data):
    num_games = extract_num_games(store_data)
    num_queries = int(num_games / get_num_games_per_query()) + 1
    return num_queries
