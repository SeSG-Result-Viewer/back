from http.client import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from fastapi import Depends, status
from sqlalchemy.orm import Session

import token_provider, sql_app.repositories.UserRepository as UserRepository
from sql_app.database import get_db

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def get_logged_in_user(token: str = Depends(oauth2_schema), session: Session = Depends(get_db)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    try:
        email = token_provider.verify_access_token(token)
    except JWTError:
        raise exception
    if not email:
        raise exception

    user = UserRepository(session).get_user_by_email(email)
    if not user:
        raise exception