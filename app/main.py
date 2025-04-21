# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from app.crawler import crawl_blog

# FastAPI 앱 생성
app = FastAPI()

# 요청 형식 정의 (카페 이름을 받을 모델)
class CafeRequest(BaseModel):
    name: str

# POST 요청을 처리할 엔드포인트 정의
@app.post("/crawl")
def crawl_cafe(data: CafeRequest):
     # ✅ 크롤링 실행
    crawl_blog(data.name)
    return {"message": f"크롤링 시작: {data.name}"}
