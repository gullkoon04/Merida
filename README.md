# Archery Club Ranking System

FastAPI를 사용한 활쏘기 클럽 랭킹 시스템입니다.

## 기능

- 학생 정보(이름, 학과, 점수) 입력
- 랭킹 조회
- 비동기 MySQL 데이터베이스 연동

## 설치 방법

1. 의존성 설치
```bash
pip install -r requirements.txt
```

2. MySQL 설정
- 데이터베이스: archery_club
- 테이블: students

3. 실행
```bash
gunicorn -c gunicorn.conf.py main:app
```

## 프로젝트 구조

```
.
├── main.py          # FastAPI 애플리케이션
├── database.py      # 데이터베이스 설정
├── dependencies.py  # 의존성 관리
├── schemas.py       # Pydantic 모델
├── templates/       # HTML 템플릿
├── static/          # 정적 파일
└── requirements.txt # 의존성 목록
```
