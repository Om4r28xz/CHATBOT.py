from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Expresion(BaseModel):
    pregunta: str
    forma_realizacion: str
    imagen_ref: Optional[str]

class Funcionalidad(BaseModel):
    pregunta: str
    descripcion: str

class HistoriaLSM(BaseModel):
    pregunta: str
    descripcion: str

class RespuestaRapida(BaseModel):
    tipo: str 
    contenido: str

class Message(BaseModel):
    pregunta: str
    descripcion: str
    timestamp: datetime


class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

