from sqlalchemy.orm import Session
from sqlalchemy import select
from .schemas import schemas
from .models import User


class UserRepository():

    @staticmethod
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create(self, user: schemas.User):
        user_bd = models.User(email=user.email,
                              id=user.id,
                              hashed_password=user.hashed_password,
                              name=user.name)
        self.session.add(user_bd)
        self.session.commit()
        self.session.refresh(user_bd)
        return user_bd

    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()

    @staticmethod
    def find_by_id(self, id) -> models.user:
        query = select(models.user).where(
            models.user.id == id)
        return self.session.execute(query).scalars().first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(models.user).filter(models.user.id == id).first() is not None
