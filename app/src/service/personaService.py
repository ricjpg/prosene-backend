from sqlalchemy.orm import Session
from ..repository.personaRepository import PersonaRepository
from ..schemas.persona import PersonaCreate, PersonaOutput
from fastapi import HTTPException

class PersonaService:
    def __init__(self, session : Session):
        self.__personaRepositoy = PersonaRepository(session=session)


    def create_persona(self, persona_details: PersonaCreate)->PersonaOutput:
        # if not self.__personaRepositoy.get_persona_by_dni(numeroidentidad=persona_details.numeroidentidad):
        #     raise HTTPException(status_code=404, detail="Numero de identidad utilizado")
        return self.__personaRepositoy.create_persona(persona_details)
    
    def get_by_user_id(self, user_id:int) -> PersonaOutput:
        self.__personaRepositoy.get_persona_by_user_id(user_id)