from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import schemas
from .models import Result

class resultRepository():

    @staticmethod
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create(self, result: schemas.Result):
        result_bd = models.Result(id=result.id,
                              graph_id=result.graph_id,
                              min_df=result.min_df,
                              Topics=result.Topics,
                              Words=result.Words,
                              No_Results_total=result.No_Results_total,
                              No_QGS=result.No_QGS,
                              No_GS_Rsts=result.No_GS_Rsts,
                              No_total_SB=result.No_total_SB,
                              Precision=result.Precision,
                              Recall=result.Recall,
                              Recall_final=result.Recall_final,
                              F1_Sts=result.F1_Sts,
                              QGS=result.QGS

                              )
        self.session.add(result_bd)
        self.session.commit()
        self.session.refresh(result_bd)
        return result_bd

    @staticmethod
    def find_all(db: Session) -> list[Result]:
        return db.query(Result).all()

    @staticmethod
    def find_by_id(self, id) -> models.result:
        query = select(models.result).where(
            models.result.id == id)
        return self.session.execute(query).scalars().first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(models.result).filter(models.result.id == id).first() is not None

    @staticmethod
    def edit(self, id: int, result: schemas.Result):
        update_stmt = update(models.Result).where(
            models.Result.id == id).values(
                              id=result.id,
                              graph_id=result.graph_id,
                              min_df=result.min_df,
                              Topics=result.Topics,
                              Words=result.Words,
                              No_Results_total=result.No_Results_total,
                              No_QGS=result.No_QGS,
                              No_GS_Rsts=result.No_GS_Rsts,
                              No_total_SB=result.No_total_SB,
                              Precision=result.Precision,
                              Recall=result.Recall,
                              Recall_final=result.Recall_final,
                              F1_Sts=result.F1_Sts,
                              QGS=result.QGS

                              )
        self.session.execute(update_stmt)
        self.session.commit()
