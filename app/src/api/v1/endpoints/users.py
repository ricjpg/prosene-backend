from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....service.userService import UserService
from ....utils.protectRoute import get_current_user

router = APIRouter(tags=["users"])


@router.post("/create", status_code=201, response_model=UserOutput, summary="Create a new user")
async def create_user(signUpDetails : UserInCreate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).signup(user_details=signUpDetails)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.get("/all", response_model=list[UserOutput], summary="Get all users")
async def get_all_users(session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_all_users()
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.get("/get/{user_id}", status_code=200, response_model=UserOutput, summary="Get user by id")
async def get_user_by_id(user_id : int, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_user_by_id(user_id=user_id)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.get("/get", status_code=200, response_model=UserOutput, summary="Get user by email")
async def get_user_by_email(email : str, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_user_by_email(email=email)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.delete("/delete", status_code=200, response_model=str, summary="Delete user")
async def delete_user(email : str, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).delete_user(email=email)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.put("/update", status_code=200, response_model=UserOutput, summary="Update user")
async def update_user(email : str, user_data : UserInUpdate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).update_user(email=email, user_data=user_data)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

