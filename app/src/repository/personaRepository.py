from .base import BaseRepository
from ..models.persona import Persona
from ..schemas.persona import PersonaCreate, PersonaOutput


class PersonaRepository(BaseRepository):
    def create_persona(self, user_data : PersonaCreate) -> PersonaOutput:
        newPersona = Persona(**user_data.model_dump(exclude_none=True))

        self.session.add(instance=newPersona)
        self.session.commit()
        self.session.refresh(instance=newPersona)
        return newPersona

    def get_persona_by_dni(self, dni : str) -> Persona:
        persona = self.session.query(Persona).filter_by(numeroidentidad=dni).first()
        return persona
    
    def get_persona_by_user_id(self, user_id : int) -> Persona:
        persona = self.session.query(Persona).filter(Persona.idusuario==user_id).first()
        return persona
    
    
    def delete_persona(self, usuario_id : str) -> str:
        persona = self.get_persona_by_id(usuario_id)
        if persona:
            self.session.delete(persona)
            self.session.commit()
            return "Persona" + persona.idusuario + " Deleted"
        raise Exception("Persona not found")
    
    def get_all_personas(self) ->list:
        try:
            personas = self.session.query(Persona).all()
            return personas
        except Exception as error:
            raise error
        