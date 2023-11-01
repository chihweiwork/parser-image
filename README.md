# Image to String
## Description
This is a project, help you to transform image to string

## install
``` bash
make install
```

## Start API Server
``` bash
make start #start parser image api server
```
## How to use
check out example folder

``` python
import base64
import requests

# read and encode image file
if __name__ == "__main__":

    path = "PATH/TO/IMAGE"
    url = "http://[API/SERVER]:[SERVICE/PORT]/base64ImageParser"

    # read image and encode to bytes-string
    with open(path, 'rb') as img_obj:
        base64_bytes = base64.b64encode(img_obj.read())
    data = {
        "file":base64_bytes
    }

    # post to api server and get result
    resp = requests.post(url=url, files=data)

    # print result
    print(resp)
``` 
