import argparse
import sys
from api_factory import APIFactory

def parse_args():
    parser = argparse.ArgumentParser(description='Query different APIs using a command-line interface.')
    parser.add_argument('api_type', help='The type of API to query (e.g., graphql, some_other_api).')
    parser.add_argument('url', help='The URL of the API endpoint.')
    parser.add_argument('query', help='The query to send to the API.')
    return parser.parse_args()

def main(args):
    try:
        api_instance = APIFactory.create_api(args.api_type)
        response = api_instance.query(args.url, args.query)
        print(response)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    arguments = parse_args()
    main(arguments)