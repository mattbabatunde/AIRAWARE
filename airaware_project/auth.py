# To get secret key that will be merged together with the username and password 
# : openssl rand -hex 32
from datetime import timedelta, datetime, timezone
from typing import Annotated
from jose import jwt
# from sqlite3 import Se
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from dotenv import load_dotenv
from database import SessionLocal, get_db
from sqlalchemy.orm import Session
import os
from models import User
from crud_op.users import user_crud

load_dotenv()


SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE = int(os.environ.get("ACCESS_TOKEN_EXPIRE"))




auth_router = APIRouter(tags=["Auth"])

class Token(BaseModel):
    access_token: str
    token_type: str



class Token_data(BaseModel):
    email: str | None = None




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

db_dependency = Annotated[Session, Depends(get_db)]


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_pwd_hash(password):
    return pwd_context.hash(password)


def get_user(db: db_dependency, email: str):
    user = user_crud.get_user_by_email(db, email)
    return user 


def authenticate_user(db: db_dependency, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    
    return user


# JWT ACCESS TOKEN
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()  # It creates a safe, editable copy of the original data so we can modify it (e.g., add expiration time) without altering the original input.
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + expires_delta(minutes=ACCESS_TOKEN_EXPIRE)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
    




def get_current_user(token: Annotated[str, Depends(oauth2_schema)], db: db_dependency):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        
        token_data = Token_data(email=email)
    except InvalidTokenError:
        raise credentials_exception
   # So essentially, this function is trying to find a user in the database who has the email address from the token.
    user = get_user(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


@auth_router.post("/token")
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],db: db_dependency) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires =timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")