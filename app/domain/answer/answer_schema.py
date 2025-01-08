from pydantic import BaseModel , field_validator
from datetime import datetime

# class Answer(BaseModel) : 
#     id : int 
#     question_id : int
#     content : str
#     create_date : datetime

#     class Config :
#         orm_mode = True 

class CreateAnswer(BaseModel) :     
    content : str
    
    @field_validator('content')
    def not_empty (cls, v) : # cls : 클래스 자체  /  v : content 필드에 전달된 값
        if not v or not v.strip() :
            raise ValueError("빈 값은 허용되지 않습니다.")
        return v

class Answer(BaseModel) : 
    id : int 
    content : str 
    create_date : datetime
