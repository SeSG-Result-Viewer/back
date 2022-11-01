from pydantic import BaseModel

class calc_body(BaseModel):
    file: list
    gs_size: int

class User(BaseModel):
    nome: str
    email: str
    senha: str

class LoginData(BaseModel):
    email: str
    senha: str