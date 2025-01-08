from fastapi import APIRouter, Depends 

from app.core.db import SessionLocal
from app.models import Question
from sqlalchemy.orm import Session
from app.domain.question import question_schema, question_crud

from app.core.db import get_db

router = APIRouter(prefix="/api/question") 

# response_model=list[question_schema.Question]의 의미는 question_list 함수의 리턴값은 Question 스키마로 구성된 리스트임을 의미
@router.get("/list", response_model=question_schema.QuestionList)
# db: Session 문장의 의미는 db 객체가 Session 타입임을 의미
def read_question_list(start_index : int , limit : int , db : Session = Depends(get_db)) : 
    # with get_db as db :
    #     _question_list = db.query(Question).order_by(Question.create_date.desc()).all() 
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all() 
    total, _question_list = question_crud.get_question_list(db, start_index, limit)
    return {"total" : total, "question_list" : _question_list}

@router.get("/question/{question_id}")
def read_question_detail(question_id : int , db : Session = Depends(get_db) ) :
    _question_detail = question_crud.get_question_detail(db, question_id=question_id)
    return _question_detail

@router.post("/question")
def create_question(_question_create : question_schema.CreateQuestion , db : Session = Depends(get_db)) : 
    question_crud.post_question(db, _question_create) 
