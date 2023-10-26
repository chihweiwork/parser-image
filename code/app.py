from fastapi import File, UploadFile, FastAPI
import shutil
import uvicorn
import traceback
import image
from typing import Dict

app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...)) -> Dict[str, str]:
    try:
        with open(f"./upload/{file.filename}", 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        lines = traceback.format_exception(type(e), e, e.__traceback__)
        return {"message": "".join(lines)}
    finally:
        file.file.close()
        
    return {"message": f"Successfully uploaded {file.filename}"}

@app.post("/imageParser")
def upload(file: UploadFile = File(...)) -> Dict[str, str]:
    try:
        upload_file_path = f"./upload/{file.filename}"
        with open(upload_file_path, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        lines = traceback.format_exception(type(e), e, e.__traceback__)
        return {"message": "".join(lines)}
    finally:
        file.file.close()

    result = image.parser(upload_file_path)
        
    return {"message": f"Successfully uploaded {file.filename}", "parser": result}


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

