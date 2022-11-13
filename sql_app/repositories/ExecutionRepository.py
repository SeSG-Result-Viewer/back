from sqlalchemy.orm import Session
from sqlalchemy import select

import sql_app.schemas as schemas
from sql_app.models import Execution

class ExecutionRepository():

    @staticmethod
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create(self, execution: schemas.Execution):
        execution_bd = Execution(
                              id=execution.id,
                              qgd=execution.qgd,
                              test_number=execution.test_number,
                              result_id=execution.result_id
                              )
        self.session.add(execution_bd)
        self.session.commit()
        self.session.refresh(execution_bd)
        return execution_bd

    @staticmethod
    def find_all(db: Session) -> list[Execution]:
        return db.query(Execution).all()

    @staticmethod
    def find_by_id(self, id) -> Execution:
        query = select(Execution).where(
            Execution.id == id)
        return self.session.execute(query).scalars().first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(Execution).filter(Execution.id == id).first() is not None

    @staticmethod
    def find_by_execution_number(self, execution_number) -> Execution:
        query = select(Execution).where(
            Execution.execution_number == execution_number)
        return self.session.execute(query).scalars().first()