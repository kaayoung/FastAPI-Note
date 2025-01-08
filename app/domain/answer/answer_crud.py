from datetime import datetime
from sqlalchemy.orm import Session
from app.models import Answer , Question
from app.domain.answer import answer_schema

def read_answers (db : Session, question_id : int) :
    _answer_list = db.query(Answer).filter(Answer.question_id == question_id).all()
    return _answer_list

def create_answer (db : Session , question : Question , answer : answer_schema.CreateAnswer) : 
    ans = Answer(question=question, content=answer.content , create_date=datetime.now())
    db.add(ans)
    db.commit()
    db.refresh(ans)
