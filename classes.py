from pydantic import BaseModel

class calc_body(BaseModel):
    file: list
    gs_size: int

# class User(BaseModel):
#     name: str
#     email: str
#     password: str

# class SimpleUser(BaseModel):
#     name: str
#     email: str

# class LoginData(BaseModel):
#     email: str
#     password: str
