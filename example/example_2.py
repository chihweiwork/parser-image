import requests
from pprint import pprint
import click

@click.command(no_args_is_help=True)
@click.option('-p', '--path', 'path', type=str, help="--path PATH/TO/IMAGE/FILE")
def main(path: str) -> None:
    img = open(path, 'rb')
    data = {
        "file":img
    }
    resp = requests.post(url=url, files=file)
    print(resp.json())


if __name__ == "__main__":


    main()
