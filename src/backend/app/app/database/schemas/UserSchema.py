from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    cod_matricula: int
    nome: str
    email: str
    senha: str
    token: str
    image_url: str
    filial_id: int
    
    class Config:
        from_attributes = True
        
class UserSchemaRegister(BaseModel):
    cod_matricula: int
    nome: str
    email: str
    senha: str
    image_url: str
    filial_id: int
    
    class Config:
        from_attributes = True
        
class UserLoginSchema(BaseModel):
    cod_matricula: int
    senha: str
    
    class Config:
        from_attributes = True

class UserPorIdSchema(BaseModel):
    id: int
      
    class Config:
        from_attributes = True