from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Dosya içeriğini okuma
    contents = await file.read()
    # Dosyayı bir yere kaydetme (örneğin, 'uploaded_file' adlı bir dosya olarak)
    with open(f"uploaded_{file.temperatures.csv}", "wb") as f:
        f.write(contents)
    return {"filename": file.temperatures.csv, "content_type": file.content_type, "size": len(contents)}

import requests

url = "http://127.0.0.1:8000/uploadfile/"
files = {"file": open("path/to/your/file.txt", "rb")}

response = requests.post(url, files=files)
print(response.json())



