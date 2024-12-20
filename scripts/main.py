import json
import os
import sys
import query_builder
import query_runner


def main():
    if len(sys.argv) > 1:
        query = json.loads(sys.argv[1])
    else:
        query = query_builder.build_query()
        print(f"\nFinal query: '{json.dumps(query)}'")

    print()
    query_runner.run_query(query)
    print(f"\nEnd of results for '{json.dumps(query)}'")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()