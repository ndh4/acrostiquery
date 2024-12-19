import json
import sys
import query_builder
import query_runner


def main():
    if len(sys.argv) > 1:
        query = json.loads(sys.argv[1])
    else:
        query = query_builder.build_query()
        print(f"\nFinal query: <python | python3 | py3 | etc.> {sys.argv[0]} {json.dumps(json.dumps(query))}")

    print()
    query_runner.run_query(query)


if __name__ == '__main__':
    main()