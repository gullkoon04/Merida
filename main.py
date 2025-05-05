from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from database import Base, engine
from schemas import Student
from dependencies import get_db
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# FastAPI 앱 초기화 & 템플릿
#    app_lifespan 함수를 통해 startup/shutdown 이벤트에서 테이블 생성 실행
async def app_lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=app_lifespan)


app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정 
templates = Jinja2Templates(directory="templates")


# 메인 페이지: 랭킹 조회 및 입력 폼 렌더링
@app.get("/")
async def read_ranking(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Student).order_by(Student.score.desc()))
    students = result.scalars().all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "students": students}
    )

# 학생 정보 제출 (폼 데이터)
@app.post("/students")
async def create_student(
    name: str = Form(...),
    department: str = Form(...),
    score: int = Form(...),
    db: AsyncSession = Depends(get_db)
):
    new_student = Student(name=name, department=department, score=score)
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return RedirectResponse(url="/", status_code=303)
