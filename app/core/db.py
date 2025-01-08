import contextlib


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread" : False}) 
## 데이터베이스와 연결을 설정하기 위해 사용
## SQLite는 기본적으로 같은 스레드에서만 연결을 허용하는데, False로 설정하면 여러 스레드에서 연결이 가능합니다.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
## SessionLocal은 데이터베이스 세션을 생성하는 팩토리 함수
##   autocommit=False: 데이터베이스 작업이 명시적으로 commit()될 때만 저장되도록 설정합니다.
##   autoflush=False: 세션이 자동으로 변경 사항을 데이터베이스에 반영하지 않도록 설정합니다.
##   bind=engine: 이 세션이 생성된 데이터베이스 엔진과 연결되도록 설정합니다.
## 생성된 세션은 데이터베이스 작업(INSERT, SELECT, UPDATE 등)을 실행할 때 사용


Base = declarative_base() 
## ORM 모델의 기본 클래스
## 데이터베이스 테이블을 Python 클래스에 매핑할 때 이 클래스를 상속받아야함


## contextlib : 컨택스트 매니저를 더 쉽게 생성하거나 관리할 수 있도록 도와주는 유틸리티 모듈
## 컨텍스트 매니저 : __enter__와 __exit__ 메서드를 정의하여 특정 리소스를 열고 닫는 동작을 자동화하는 객체

# @contextlib.contextmanager
def get_db() : 
    db = SessionLocal()
    try : 
        # yield : 함수 실행을 잠시 멈추고, 호출자에게 db 객체를 반환
        # 호출자가 with 블록 안에서 db 객체를 사용하여 데이터베이스 작업을 수행할 수 있습니다.
        yield db 
    finally : 
        db.close() 
