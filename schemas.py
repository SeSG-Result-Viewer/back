from typing import Optional #, ItemsView, List, Union 

from pydantic import BaseModel 
#import models

class User(BaseModel):
    name: str
    email: str
    hashed_password: str
    id: Optional[int] = None

    # projects: Optional[List[Project]] = []
    
    class Config:
        orm_mode = True
        
class SimpleUser(BaseModel):
    email: str
    name: str

    #projects: Optional[List[Project]] = []

class LoginData(BaseModel):
    email: str
    password: str

class SucessLogin(BaseModel):
    usuario: SimpleUser
    access_token: str

class calc_body(BaseModel):
    file: list
    gs_size: int

""" class Project(BaseModel):
    id: Optional[int] = None
    author: str
    execution_number: int

    user: str
        
    class Config:
        orm_mode = True

class Result (BaseModel):
    id: Optional[int] = None
    graph_id: int
    min_df: float
    Topics: int
    Words: int
    Similar_Words: int
    No_Results_total: int
    No_QGS: int
    No_GS_Rsts: int
    No_total_SB: int
    Precision: float
    Recall: float
    Recall_final: float
    F1_Sts: float
    QGS: int 
    
    exec: str
        
    class Config:
        orm_mode = True
        
class Execution(BaseModel):
    id: Optional[int] = None
    qgd: str 
    test_number: int
    result_id: int

    results: Optional[List[Result]] = []
    
    class Config:
        orm_mode = True """