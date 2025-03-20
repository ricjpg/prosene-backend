from fastapi import FastAPI, Depends, APIRouter
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....service.userService import UserService
from ....utils.protectRoute import get_current_user


router = APIRouter(tags=["auth"])

@router.post("/login", status_code=200, response_model=UserWithToken)
def login(loginDetails: UserInLogin, session: Session = Depends(get_db)):
    try:
        return UserService(session=session).login(login_details=loginDetails)
    except Exception as error:
        print(error)
        raise error


# Descripcion: Este endpoint se encarga de registrar un nuevo usuario, desactivado para produccion 

@router.post("/signup", status_code=201, response_model=UserOutput)
def signUp(signUpDetails : UserInCreate, session : Session = Depends(get_db)):
    try:
        return UserService(session=session).signup(user_details=signUpDetails)
    except Exception as error:
        print(error)
        raise error
    
@router.get("/me", status_code=200, response_model=UserOutput)
def me(session: Session = Depends(get_db), user: UserOutput = Depends(get_current_user)):
    return user