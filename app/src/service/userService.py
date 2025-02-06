from ..repository.userRepository import UserRepository
from ..schemas.user import UserInLogin, UserOutput, UserWithToken, UserInCreate, UserInUpdate
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
        
        user = self.__userRepository.get_user_by_email(email=login_details.email)
        if HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password):
            token = AuthHandler.sign_jwt(user_id=user.id, role_id=user.role_id)
            if token:
                return UserWithToken(token=token)
            raise HTTPException(status_code=500, detail="Unable to process request")
        raise HTTPException(status_code=400, detail="Please check your Credentials")
    
    def delete_user(self, email : str) -> str:
        if self.__userRepository.user_exist_by_email(email=email):
            return self.__userRepository.delete_user(email=email)
        raise HTTPException(status_code=404, detail="User not found")
    
    def get_user_by_email(self, email : str) -> UserOutput:
        user = self.__userRepository.get_user_by_email(email=email)
        if user:
            return user
        raise HTTPException(status_code=404, detail="User not found")
    
    def get_user_by_id(self, user_id : int) -> UserOutput:
        user = self.__userRepository.get_user_by_id(user_id=user_id)
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
            hashed_password = HashHelper.get_password_hash(plain_password=user_data.password)
            user_data.password = hashed_password
            user = self.__userRepository.update_user(email=email, user_data=user_data)
            print(hashed_password)
            return user
        raise HTTPException(status_code=404, detail="User not found")