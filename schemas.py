from typing import ItemsView, List, Union, Optional

from pydantic import BaseModel 
import models

class Project(BaseModel):
    id: int
    author: str
    execution_number: int

    user: str
        
    class Config:
        orm_mode = True

class User(BaseModel):
    email: str
    id: int
    hashed_password: str
    name: str

    projects: List[Project] = []
    
    class Config:
        orm_mode = True
        
class UserSimple(BaseModel):
    email: str
    id: int
    name: str

    projects: List[Project] = []
    
    class Config:
        orm_mode = True

class Result (BaseModel):
    id: int
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
    id: int
    qgd: str 
    test_number: int
    result_id: int

    results: List[Result] = []
    
    class Config:
        orm_mode = True
