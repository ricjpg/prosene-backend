import jwt
import os
import time
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


class AuthHandler(object):

    @staticmethod
    def sign_jwt(user_id : int, role_id : int) -> str:
        payload = {
            "user_id" : user_id,
            "expires": time.time() + 12000,
            "role_id": role_id
        }

        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return token

    @staticmethod
    def decode_jwt(token : str) -> dict:
        try:
            decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except:
            print("unable to decode the token")
            return None
        
    @staticmethod
    def decode_token(token:str) -> dict:
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            return decoded
        except:
            print("unable to decode")
            return None
            