# 1) 베이스 이미지
FROM python:3.10-slim

# 2) 작업 디렉터리 생성
WORKDIR /app

# 3) 의존성만 복사 & 설치 (빌드 캐시 활용)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) 소스코드 복사
COPY . .

# 5) 컨테이너 포트 노출
EXPOSE 8000

# 6) 디폴트 실행 커맨드
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
