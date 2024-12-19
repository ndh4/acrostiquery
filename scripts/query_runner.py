from SearchSpace import make_search_space
from do_search import do_search

def run_query(query) -> None:
    search_space = make_search_space(query['search_space'], query['lang'])
    results = do_search(query['mode'], query['lang'],
              search_space,
              query['term'], query['buflen'])
    print(results.to_string())