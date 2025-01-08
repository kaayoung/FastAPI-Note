from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo

class SignUpUser (BaseModel) :
    user_name : str 
    password : str 
    password2 : str
    email : EmailStr 

    @field_validator('user_name' , 'password' , 'password2' , 'email')
    def not_empty(cls, v) : 
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다')
        return v
    
    @field_validator('password2') 
    def not_same(cls, v, info : FieldValidationInfo) : 
        if 'password' in info.data and v != info.data['password'] : 
            raise ValueError("비밀번호가 일치하지 않습니다.") 
        return v 

class Token(BaseModel) : 
    access_token : str 
    token_type : str 
    user_name : str 
    
