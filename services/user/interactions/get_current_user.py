
from fastapi import Depends, HTTPException
import jwt
from services.user.constants.user_typical_constants import USER_SESSION_ALGORITHM
from configs.env import SECRET_KEY

from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )   

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[USER_SESSION_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired", headers={"WWW-Authenticate": "Bearer"})
    except jwt.JWTError:
        raise credentials_exception

    return username
