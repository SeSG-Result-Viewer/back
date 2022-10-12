from typing import ItemsView, List, Union, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    id: int
    hashed_password: str
    name: str

    projects: List[Item] = []

class Project(BaseModel):
    id: int
    author: str
    execution_number: int

    user: str
    
class Execution(BaseModel):
    id: int
    qgd: str 
    test_number: int
    result_id: int

    results: List[Item] = []

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
