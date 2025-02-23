from typing import List
from fastapi import FastAPI, Depends, APIRouter, Header, HTTPException, status,Request, Form
from ....schemas.user import UserInCreate, UserInLogin, UserWithToken, UserOutput, UserInUpdate, ResetPassword
from ....database.database import get_db
from sqlalchemy.orm import Session
from ....service.userService import UserService
from ....utils.protectRoute import get_current_user
from ....service.personaService import PersonaService
from ....schemas.persona import PersonaCreate, PersonaOutput
from ....service.solicitudService import SolicitudService
from ....schemas.solicitudes import SolicitudesCreate, SolicitudesOutput
from ....schemas.formulario import FormularioCreate, FormularioOutput
from ....service.formularioService import FormularioService
from ....schemas.email import EmailSchema
import smtplib, os
from email.message import EmailMessage
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

load_dotenv()

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
async def get_all_users(session : Session = Depends(get_db))->list[UserOutput]:
    # if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_all_users()
        except Exception as error:
            print(error)
            raise error
    # raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.get("/get/{user_id}", status_code=200, response_model=UserOutput, summary="Get user by id")
async def get_user_by_id(user_id : int, session : Session = Depends(get_db)):
    # if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_user_by_id(user_id=user_id)
        except Exception as error:
            print(error)
            raise error
    # raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.get("/get", status_code=200, response_model=UserOutput, summary="Get user by email")
async def get_user_by_email(email : str, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).get_user_by_email(email=email)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.put("/delete", status_code=200, response_model=str, summary="Delete user")
async def delete_user(email : str, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    # if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).delete_user(email=email)
        except Exception as error:
            print(error)
            raise error
    # raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")

@router.put("/update", status_code=200, response_model=UserOutput, summary="Update user")
async def update_user(email : str, user_data : UserInUpdate, session : Session = Depends(get_db), user : UserOutput = Depends(get_current_user)):
    if user.role_id == 1 or user.role_id == 2:
        try:
            return UserService(session=session).update_user(email=email, user_data=user_data)
        except Exception as error:
            print(error)
            raise error
    raise HTTPException(status_code=403, detail="Unauthorized, please contact the admin")


@router.post("/detalles_personales", status_code=200, summary="Detalles personales del usuario")
async def add_details(persona_input : PersonaCreate, session : Session = Depends(get_db)) -> PersonaOutput:
    try:
        return PersonaService(session=session).create_persona(persona_details=persona_input)
    except Exception as error:
        print(error)
        raise error

@router.get("/formulario/{id}", status_code=200, summary="Obtener formulario completo")
async def get_full_form(id : int, session : Session = Depends(get_db)):
    try:
        return FormularioService(session=session).get_form_by_user_id(user_id=id)
    except Exception as error:
        print(error)
        raise error

@router.post("/resetpassword/{emailInput}", status_code=200, summary="reset password")
async def reset_password(email_input:str, data:ResetPassword ,session : Session = Depends(get_db)):
    data.email = email_input
    user = UserService(session=session).get_user_by_email(data.email)
    if user:
        try:
            return UserService(session=session).reset_password(email=data.email, password=data.password)
        except Exception as error:
            print(error)
            raise error
    return HTTPException(status_code=404, detail="usuario no encontrado")

@router.post("/requestreset", status_code=200, summary="reques password reset")
async def reset_password(mail_data : EmailSchema, session : Session=Depends(get_db)):
    try:
        user = UserService(session=session).get_user_by_email(mail_data.emailAddress)
        persona = PersonaService(session=session).get_by_user_id(user.idusuario)
        user_token =  UserService(session=session).generete_token(mail_data.emailAddress)
        email_address = os.getenv('email_address')
        email_password = os.getenv('email_password')
        
        # create email
        msg = EmailMessage()
        msg['Subject'] = "Reset Password Request"
        msg['From'] = email_address
        msg['To'] = os.getenv('email_destination')
        msg.set_content(
        f"""\
        <html>
            <body>
                <p>Hi !!!
                    <br>Al parecer olvidaste tu contraseña, no te preocupes 😁</p>
                    <p>
                    <br>Para cambiar tu contraseña accede al siguiente enlace: </p>
                <a href="http://localhost:8000/api/v1/users/resetpassword/?emailInput={mail_data.emailAddress}" class="button">Cambiar mi contraseña</a>
            </body>
        </html> 
        """, "html"
        )

        # msg.set_default_type("html")
        # send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
    
        return "email successfully sent"
    except Exception as error:
        print(error)
        return error