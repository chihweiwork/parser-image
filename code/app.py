from fastapi import File, UploadFile, FastAPI
import shutil
import uvicorn
import traceback
import image
import base64
import pdb
from PIL import Image
from io import BytesIO
from typing import Dict

app = FastAPI()

@app.post("/base64ImageParser")
def base64ImageParser(file: UploadFile = File(...)) -> Dict[str, str]:
    """
    Get data from post request and parser image and get string in image.
    """
    try:
        result = image.parser_in_memory(file.file.read())
        return {"message": f"Successfully uploaded {file.filename}", "parser": result}
        
    except Exception as e:
        lines = traceback.format_exception(type(e), e, e.__traceback__)
        return {"message": "".join(lines)}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

