from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def readroot():
    return {"status":"backend running"}


