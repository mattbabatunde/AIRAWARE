from fastapi import APIRouter, HTTPException, status, Depends
from schemas.user import User, UserCreate, UserDb, UserUpdate, UserPasswordUpdate
from sqlalchemy.orm import Session
from database import get_db
from typing import Annotated
from auth import get_pwd_hash, verify_password
from crud_op.users import user_crud






user_router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@user_router.post("/")
def create_user(db: db_dependency,  user: UserCreate):
    return user_crud.create_user(user, db)



@user_router.get("/")
def get_all_users(db: db_dependency):
    users = user_crud.get_all_users(db)
    return users



@user_router.get("/{user_id}")
def get_user(user_id: str, db: db_dependency):
    user = user_crud.get_users(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@user_router.get("/by-username/{username}")
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@user_router.get("/by-email/{email}")
def get_user_by_username(email: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_router.put("/{user_id}")
def update_user(user_id: str, update_user: UserUpdate, db: db_dependency):
    updated_user = user_crud.update_user(db, user_id, update_user)
    if not update_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return update_user



@user_router.put("/password/{user_id}")
def update_user_password(user_id: str, user_data: UserPasswordUpdate, db: db_dependency):
    db_user = user_crud.get_users(db, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(user_data.current_password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    return user_crud.update_password(db, user_id, new_password=user_data.current_password)



@user_router.delete("/{user_id}")
def delete_user(user_id: str, db: db_dependency):
    db_user = user_crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Deleted successfully"}

