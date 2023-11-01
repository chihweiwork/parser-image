import requests
from PIL import Image
import base64
import click
import pdb

def read_image(path:str) -> bytes:
    with open(path, 'rb') as img_obj:
        base64_bytes = base64.b64encode(img_obj.read())
        return base64_bytes

@click.command(no_args_is_help=True)
@click.option('--path', 'path', type=str, help="--path PATH/TO/IMAGE/FILE")
@click.option('--url', 'url', type=str, help="--url API/URL")
def main(path: str, url: str) -> None:

    img_string = read_image(path)
    data = {
        "file": img_string
    }

    resp = requests.post(url=url, files=data)
    print(resp.json())

if __name__ == "__main__":

    main()
