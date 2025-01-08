import datetime

from pydantic import BaseModel , field_validator
from app.domain.answer import answer_schema

# Pydantic의 BaseModel은 다음과 같은 목적으로 사용됩니다:
## -데이터 유효성 검증 (Validation).
## -JSON 데이터를 Python 객체로 역직렬화 (Parsing).
## -Python 객체를 JSON으로 직렬화 (Serialization).
## -FastAPI와 결합하여 요청/응답 데이터 구조를 정의.

class Question(BaseModel) :
    id: int
    subject: str
    content: str
    create_date: datetime.datetime
    answers : list[answer_schema.Answer] = []

    class Config:
        orm_mode = True

class CreateQuestion(BaseModel) : 
    subject : str 
    content : str 
    @field_validator('subject' , 'content') 
    def not_empty(cls, v) :
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class QuestionList(BaseModel) : 
    total : int = 0 
    question_list : list[Question] = [] 
