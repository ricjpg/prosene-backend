from .base import BaseRepository
from ..models.user import User
from ..schemas.user import UserInCreate, UserOutput, UserInUpdate


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
    
    def get_user_by_id(self, user_id : int) -> User:
        user = self.session.query(User).filter_by(id=user_id).first()
        return user
    
    
    def delete_user(self, email : str) -> str:
        user = self.get_user_by_email(email)
        if user:
            self.session.delete(user)
            self.session.commit()
            return "User" + user.email + " Deleted"
        raise Exception("User not found")
    
    def get_all_users(self) ->list:
        try:
            return self.session.query(User).all()
        except Exception as error:
            raise error
        
    def update_user(self, email : str, user_data : UserInUpdate) -> UserOutput:
        user = self.get_user_by_email(email)
        if user:
            user.first_name = user_data.first_name
            user.last_name = user_data.last_name
            user.email = user_data.email
            user.password = user_data.password
            user.role_id = user_data.role_id
            self.session.commit()
            self.session.refresh(instance=user)
            return user
        raise Exception("User not found")