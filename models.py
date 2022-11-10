from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    #projects = relationship("Project", back_populates = "user")
""" 
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    author = Column(String, index=True)

    id_author = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates = "projects")

    executions = relationship("Execution", back_populates = "projects")

class Execution(Base):
    __tablename__ = "executions"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    qgs = Column(String, index = True)

    results = relationship("Result", back_populates="executions", uselist=False)

    id_project = Column(Integer, ForeignKey("projects.id"))
    projects = relationship("Project", back_populates = "executions")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True, autoincrement = True)
    graph_id = Column(Integer, index=True)
    min_df = Column(Float)
    topics = Column(Integer)
    words = Column(Integer)
    similar_words = Column (Integer)
    no_results_total = Column(Integer)
    no_qgs = Column(Integer)
    no_gs_rsts = Column(Integer)
    no_total_sb = Column(Integer)
    precision = Column(Float)
    recall = Column(Float)
    recall_final = Column(Float)
    f1_sts = Column(Float)
    qgs = Column(Integer)

    id_execution = Column(Integer, ForeignKey("executions.id"))

    executions = relationship("Execution", back_populates = "results") """