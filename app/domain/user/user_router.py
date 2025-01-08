from fastapi import APIRouter, Depends , HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.db import  get_db
from app.domain.user import user_schema, user_crud
from datetime import datetime 

router = APIRouter(prefix="/api/user")

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = "4ab2fce7a6bd79e1c014396315ed322dd6edb1c5d975c6b74a2904135172c03c"
ALGORITHM = "HS256"


@router.post("/signup")
def create_user(user_create : user_schema.SignUpUser, db : Session = Depends(get_db)) : 
    user_crud.create_user(db=db , user_create=user_create)


@router.post("/login", response_model=user_schema.Token) 
def login_for_access_token (form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)) :
    user = user_crud.get_user(db, form_data.username) 
    if not user or not user_crud.pwd_context.verify(form_data.password , user.password) : 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="아이디 혹은 비밀번호가 틀립니다" , 
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    data = {
        "sub" : user.user_name, 
        # "exp" : datetime. + 
    }
