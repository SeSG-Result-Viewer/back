from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import schemas
from .models import Project


class ProjectRepository():

    @staticmethod
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create(self, project: schemas.Project):
        project_bd = models.Project(
                              id=project.id,
                              author=project.author,
                              execution_number=project.execution_number,
                              )
        self.session.add(project_bd)
        self.session.commit()
        self.session.refresh(project_bd)
        return project_bd

    @staticmethod
    def find_all(db: Session) -> list[Project]:
        return db.query(Project).all()

    @staticmethod
    def find_by_id(self, id) -> models.project:
        query = select(models.project).where(
            models.project.id == id)
        return self.session.execute(query).scalars().first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(models.project).filter(models.project.id == id).first() is not None
