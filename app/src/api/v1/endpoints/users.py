from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput
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
