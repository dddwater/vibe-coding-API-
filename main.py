from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello"}

@app.get("/")
def root():
    return {"message": "Hello"}


# 健康檢查
@app.get("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# 關於資訊
@app.get("/about")
def about():
    return {
        "project": "Render Test API",
        "author": "zack",
        "framework": "FastAPI"
    }