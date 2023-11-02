import requests
from PIL import Image
import base64
import click
import pdb

def read_image(path:str) -> bytes:
    """
    Function to read image and return bytes-string
    """
    with open(path, 'rb') as img_obj:
        base64_bytes = base64.b64encode(img_obj.read())
        return base64_bytes

@click.command(no_args_is_help=True)
@click.option('--path', 'path', type=str, help="--path PATH/TO/IMAGE/FILE")
@click.option('--url', 'url', type=str, help="--url API/URL")
def main(path: str, url: str) -> None:
    """
    post image path and api url to parser image, get string in image.
    """

    img_string = read_image(path)
    data = {
        "filename": path,
        "body": img_string.decode('utf-8')
    }

    resp = requests.post(url=url, json=data)
    print(resp.json())

if __name__ == "__main__":

    main()
