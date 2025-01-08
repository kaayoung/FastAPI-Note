from sqlalchemy.orm import Session
from app.domain.user import user_schema
from app.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

def create_user(db : Session, user_create : user_schema.SignUpUser) :
    user = User(user_name = user_create.user_name , password = user_create.password, email=user_create.email )
    db.add(user)
    db.commit() 

def get_user(db : Session , user_name : str) :
    return db.query(User).filter(User.user_name == user_name).first() 
