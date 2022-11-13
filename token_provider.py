from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = '449f2562136bd59e79e4cf8c683481ff'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 24 * 10 * 60       #Tempo ate expirar

def create_access_token(data: dict):
    data1 = data.copy()
    expiry = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    data1.update({'exp': expiry})
    token_jwt = jwt.encode(data1, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt


def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    return payload.get('sub')