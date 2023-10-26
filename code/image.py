from PIL import Image
import pytesseract

def parser(path: str) -> str:

    img = Image.open(path)
    text = pytesseract.image_to_string(img, lang='eng')

    #text = " ".join(text.splitlines())
    return text
