import argparse

from SearchSpace import make_search_space
from do_search import do_search


def run_cmd() -> None:
    parser = argparse.ArgumentParser(
        prog='acrostiquery',
        description='Searches for acrostics in the file or directory given')
    parser.add_argument('pathname')
    parser.add_argument('term')
    parser.add_argument('-m', '--search-mode')
    parser.add_argument('-l', '--language')
    parser.add_argument('-b', '--buffer-length', type=int)

    args = parser.parse_args()
    search_space = make_search_space(args.pathname, args.language)
    results = do_search(args.search_mode, args.language,
              search_space,
              args.term, args.buffer_length)
    print(results.to_string())

if __name__ == '__main__':
    run_cmd()