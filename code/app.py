from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import traceback
from code import image
from typing import Dict
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5000",
    "http://localhost:80",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Base64ImageRequest(BaseModel):
    filename: str
    body: str

@app.post("/base64ImageParser")
def base64ImageParser(image_base64_request: Base64ImageRequest) -> Dict[str, str]:
    """
    Get data from post request and parser image and get string in image.
    """
    try:
        result = image.parser_in_memory(image_base64_request.body)
        return {"message": f"Successfully uploaded {image_base64_request.filename}", "parser": result}
        
    except Exception as e:
        lines = traceback.format_exception(type(e), e, e.__traceback__)
        return {"message": "".join(lines)}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

