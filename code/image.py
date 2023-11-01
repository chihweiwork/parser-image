from PIL import Image
import io
import pytesseract
import pdb
import base64

def parser_in_memory(base64_string: bytes) -> str:
    img = Image.open(
        io.BytesIO(
            base64.decodebytes(base64_string)
        )
    )
    
    
    return pytesseract.image_to_string(img, lang='eng')
