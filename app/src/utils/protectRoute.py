from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated, Union
from ..core.security.authHandler import AuthHandler
from ..service.userService import UserService
from ..database.database import get_db
from ..schemas.user import UserWithToken, UserOutput

AUTH_PREFIX = 'Bearer '

def get_current_user(
        session : Session = Depends(get_db), 
        authorization : Annotated[Union[str, None] , Header()] = None 
) -> UserOutput:
    auth_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Invalid Authentication Credentials"
    )
   
    if not authorization:
        raise auth_exception

    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception

    payload = AuthHandler.decode_jwt(token=authorization[len(AUTH_PREFIX):])

    if payload and payload["user_id"]:
        try:
            user = UserService(session=session).get_user_by_id(payload["user_id"])
            return UserOutput(
                idusuario = user.idusuario,
                email=user.email,
                role_id=user.role_id,
                isactive=user.isactive
            )
        except Exception as error:
            raise error
    raise auth_exception
    