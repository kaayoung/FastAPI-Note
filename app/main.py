from fastapi import FastAPI
from app.domain.question import question_router
from app.domain.answer import answer_router
from app.domain.user import user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
