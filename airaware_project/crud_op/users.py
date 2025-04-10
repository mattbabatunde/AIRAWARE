from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas.user import  UserCreate,  UserDb, UserUpdate
from models import User
from utils import get_pwd_hash
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException



class UserCrud:


    @staticmethod
    def create_user( user: UserCreate, db: Session):
        hashed_pass = get_pwd_hash(user.password)
        db_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            email=user.email,
            hashed_password=hashed_pass,
            created_at=datetime.utcnow()
        )
        
        db.add(db_user)
 
        try:
            db.commit()
            db.refresh(db_user)
        except IntegrityError as e:
            db.rollback()  
            if "users_username_key" in str(e.orig):
                raise HTTPException(status_code=400, detail="Username already exists")
            elif "users_email_key" in str(e.orig):
                raise HTTPException(status_code=400, detail="Email already exists")
            else:
               raise HTTPException(status_code=400, detail="Invalid input")

        return db_user
    

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()


    @staticmethod
    def get_users(db: Session, user_id: str):
        return db.get(User, user_id)
    

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
    
        
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first() 


    @staticmethod
    def update_user(db: Session, user_id: str, update_user: UserUpdate, ):
         db_user = db.get(User, user_id)
         if not db_user:
             return None
         user_data = update_user.dict()
         for key, value in user_data.items():
             setattr(db_user, key, value)

         db.commit()
         db.refresh(db_user)
         return db_user
     
    
    @staticmethod
    def update_password(db: Session, user_id: str, new_password: str):
        db_user = db.get(User, user_id)
        if db_user:
            db_user.hashed_password = get_pwd_hash(new_password)
            db.commit()
            db.refresh(db_user)

        return db_user
    
    
    @staticmethod
    def delete_user(db: Session, user_id: str):
        db_user = db.get(User, user_id)
        if db_user:
            db.delete(db_user)
            db.commit()
        return db_user
         

user_crud = UserCrud()

