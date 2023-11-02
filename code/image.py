from PIL import Image
import io
import pytesseract
import base64

def parser_in_memory(base64_string: str) -> str:
    """
    Decode image bytes-string and open by PLI.
    Parser image data from pytesseract.
    Return string on image.
    """
    img = Image.open(
        io.BytesIO(
            base64.decodebytes(base64_string.encode('utf-8'))
        )
    )

    return pytesseract.image_to_string(img, lang='eng')
