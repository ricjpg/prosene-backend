from .base import BaseRepository
from ..models.user import User
from ..schemas.user import UserInCreate, UserOutput, UserInUpdate, ResetPassword
from fastapi import HTTPException


class UserRepository(BaseRepository):
    def create_user(self, user_data : UserInCreate):
        newUser = User(**user_data.model_dump(exclude_none=True))

        self.session.add(instance=newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)
        return newUser

    def user_exist_by_email(self, email : str) -> bool:
        user = self.session.query(User).filter_by(email=email).first()
        return bool(user)

    def get_user_by_email(self, email : str) -> User:
        user = self.session.query(User).filter_by(email=email).first()
        return user
    
    def get_user_by_id(self, user_id : int) -> UserOutput:
        user = self.session.query(User).filter_by(idusuario=user_id).first()
        return user
    
    
    def delete_user(self, email : str) -> str:
        user = self.get_user_by_email(email)
        if user and user.isactive==True:
            user.isactive = False
            self.session.commit()
            return "User: " + user.email + " Deleted"
        return "User not found"
    
    def get_all_users(self) ->list[UserOutput]:
        try:
            users = self.session.query(User).filter(User.isactive==True).all()
            return users
        except Exception as error:
            raise error
        
    def update_user(self, email : str, user_data : UserInUpdate) -> UserOutput:
        user = self.get_user_by_email(email)
        if user:
            user.email = user_data.email
            # user.password = user_data.password
            user.role_id = user_data.role_id
            user.idcentroregional = user_data.idcentroregional
            self.session.commit()
            self.session.refresh(instance=user)
            return user
        raise Exception("Usuario no encontrado")

    def reset_password(self, user_data: ResetPassword) -> str:
        user = self.get_user_by_email(user_data.email)
        print(user)
        if user:
            user.password = user_data.password
            self.session.commit()
            self.session.refresh(instance=user)
            return "Se ha cambiado tu contraseña"
        return HTTPException(status_code=404, detail="Usuario no encontrado")