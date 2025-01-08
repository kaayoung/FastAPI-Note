from fastapi import APIRouter , Depends , HTTPException
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.domain.answer import answer_crud, answer_schema
from app.domain.question import question_crud
from starlette import status

router = APIRouter(prefix="/api/answer")

@router.get("/{question_id}/answers") 
def get_answers(question_id : int ,db : Session = Depends(get_db)) : 
    _answers_list = answer_crud.read_answers(db, question_id) 
    return _answers_list

@router.post("/create/{question_id}",status_code=status.HTTP_204_NO_CONTENT)
def post_answer(question_id : int ,answer : answer_schema.CreateAnswer, db : Session = Depends(get_db)) : 
    question = question_crud.get_question_detail(db,question_id=question_id) 
    if not question :
        raise HTTPException(status_code=404,  detail="Question not found")
    
    answer_crud.create_answer(db=db , question=question , answer=answer)

