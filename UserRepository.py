from sqlalchemy.orm import Session
from sqlalchemy import select

import schemas
from models import User


class UserRepository():

    @staticmethod
    def __init__(self, session: Session):
        self.session = session

    @staticmethod
    def create(self, user: schemas.User):
        user_bd = User(email=user.email,
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
    def find_by_id(self, id) -> User:
        query = select(User).where(
            User.id == id)
        return self.session.execute(query).scalars().first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
