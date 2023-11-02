from PIL import Image
import pytesseract
import pdb
import click
  

@click.command(no_args_is_help=True)
@click.option("-t", "--target", 'target', type=str, help="--target PATH/TO/IMAGE/FILE")
def main(target):
    # img = Image.open(target)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)


if __name__ == "__main__":

    main()
