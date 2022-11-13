from sqlalchemy.orm import Session
from sqlalchemy import select

import schemas
from models import User

class UserRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        user_db = User( name=user.name,
                        email=user.email,
                        hashed_password=user.hashed_password)
        self.session.add(user_db)
        self.session.commit()
        self.session.refresh(user_db)
        return user_db

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