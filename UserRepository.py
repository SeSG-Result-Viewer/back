from sqlalchemy.orm import Session
from sqlalchemy import select

import schemas
from models import User


class UserRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        user_bd = User(email=user.email,
                              id=user.id,
                              hashed_password=user.hashed_password,
                              name=user.name)
        self.session.add(user_bd)
        self.session.commit()
        self.session.refresh(user_bd)
        return user_bd

    def find_all(self) -> list[User]:
        return self.session.query(User).all()

    def find_by_id(self, id) -> User:
        query = select(User).where(
            User.id == id)
        return self.session.execute(query).scalars().first()

    def exists_by_id(self, id: int) -> bool:
        return self.session.query(User).filter(User.id == id).first()
    
    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    # def get_user_by_email(self, email) -> User:
    #     query = select(User).where(
    #         User.email == email)
    #     return self.session.execute(query).scalars().first()
    