from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    name = Column(String, unique=True, index=True, nullable=False)

    projects = relationship("Project", back_populates = "user")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    author = Column(String, index=True)
    execution_number = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates = "projects")

class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    qgs = Column(String, index = True)
    test_number = Column(Integer, ForeignKey("results.QGS"))
    result_id = Column(Integer, ForeignKey("results.id") )

    results = relationship("Result", back_populates="exec")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    graph_id = Column(Integer, index=True)
    min_df = Column(Float)
    Topics = Column(Integer)
    Words = Column(Integer)
    Similar_Words = Column (Integer)
    No_Results_total = Column(Integer)
    No_QGS = Column(Integer)
    No_GS_Rsts = Column(Integer)
    No_total_SB = Column(Integer)
    Precision = Column(Float)
    Recall = Column(Float)
    Recall_final = Column(Float)
    F1_Sts = Column(Float)
    QGS = Column(Integer) #(numero do teste, que vem da tabela execução) 

    exec = relationship("Execution", back_populates = "results")

