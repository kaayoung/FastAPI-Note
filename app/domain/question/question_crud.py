from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Question
from app.domain.question import question_schema

def get_question_list (db : Session, start_index : int = 0 , limit : int = 0 ) :
    question_list = db.query(Question).order_by(Question.create_date.desc())
    # 세션.query(모델)

    total = question_list.count() 
    question_list = question_list.offset(start_index).limit(limit).all() 
    return total, question_list

def get_question_detail (db : Session , question_id : int) :
    question_detail = db.query(Question).filter(Question.id == question_id).first()
    return question_detail

def post_question (db : Session , post : question_schema.CreateQuestion) : 
    q = Question(subject = post.subject , content = post.content, create_date=datetime.now())
    db.add(q)
    db.commit() 
    db.refresh(q)
