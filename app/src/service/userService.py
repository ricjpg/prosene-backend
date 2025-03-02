from ..repository.userRepository import UserRepository
from ..schemas.user import UserInLogin, UserOutput, UserWithToken, UserInCreate, UserInUpdate, ResetPassword
from ..core.security.hashHelper import HashHelper
from ..core.security.authHandler import AuthHandler
from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..schemas.user import UserOutput

class UserService:
    def __init__(self, session : Session):
        self.__userRepository = UserRepository(session=session)
    
    def signup(self, user_details : UserInCreate) -> UserOutput:
        if self.__userRepository.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=400, detail="Please Login")
        
        hashed_password = HashHelper.get_password_hash(plain_password=user_details.password)
        user_details.password = hashed_password
        return self.__userRepository.create_user(user_data=user_details)
    
    def login(self, login_details : UserInLogin) -> UserWithToken:
        if not self.__userRepository.user_exist_by_email(email=login_details.email):
            raise HTTPException(status_code=400, detail="Please create an Account")
        if not self.__userRepository.get_user_by_email(email=login_details.email).isactive==True:
            raise HTTPException(status_code=400, detail="Account deactivate, please contact the administrator")
        
        user = self.__userRepository.get_user_by_email(email=login_details.email)
        if HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password):
            token = AuthHandler.sign_jwt(user_id=user.idusuario, role_id=user.role_id)
            if token:
                return UserWithToken(token=token, idusuario=user.idusuario, role_id=user.role_id, isActive=user.isactive)
            raise HTTPException(status_code=500, detail="Unable to process request")
        raise HTTPException(status_code=400, detail="Please check your Credentials")
    
    def delete_user(self, email : str) -> str:
        if self.__userRepository.user_exist_by_email(email=email):
            return self.__userRepository.delete_user(email=email)
        raise HTTPException(status_code=404, detail="User not found")
    
    def get_user_by_email(self, email : str):
        user = self.__userRepository.get_user_by_email(email=email)
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    
    def get_user_by_id(self, user_id : int) -> UserOutput:
        user = self.__userRepository.get_user_by_id(user_id)
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")

    def get_all_users(self) -> list[UserOutput]:
        try:
            return self.__userRepository.get_all_users()
        except Exception as error:
            raise HTTPException(status_code=500, detail="Unable to process request")
    
    def update_user(self, email:str, user_data : UserInUpdate) -> UserOutput:
        user = self.get_user_by_email(email)
        if user:
            # hashed_password = HashHelper.get_password_hash(plain_password=user_data.password)
            # user_data.password = hashed_password
            user = self.__userRepository.update_user(email=email, user_data=user_data)
            # print(hashed_password)
            return user
        raise HTTPException(status_code=404, detail="User not found")
    
    def generete_token(self, email_input: str) -> str:
        user = self.__userRepository.get_user_by_email(email_input)
        print(user)
        token = AuthHandler.sign_jwt(user_id=user.idusuario, role_id=user.role_id)
        
        if token:
            print(token)
            return token
        raise HTTPException(status_code=500, detail="Unable to process request")
    
    def reset_password(self, email:str, password:str)->str:
        user = self.get_user_by_email(email)
        print(user)
        if user:
            hashed_password = HashHelper.get_password_hash(plain_password=password)
            user.password = hashed_password
            user = self.__userRepository.reset_password(user_data=user)
            return user
        return HTTPException(status_code=404, detail="user not found")
    
    
    def get_payload(self, token:str):
        token_data = AuthHandler.decode_token(token)
        print(token_data)
        return token_data
    
