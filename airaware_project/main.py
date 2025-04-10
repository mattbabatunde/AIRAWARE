from fastapi import FastAPI, HTTPException, status
from routers import users
from database import engine
from models import Base
import auth



app = FastAPI()
app.include_router(users.user_router, tags=["User"], prefix="/users")
app.include_router(auth.auth_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return{"msg": "Welcome where lives are saved"}





