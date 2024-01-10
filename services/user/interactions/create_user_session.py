
from services.user.constants.user_typical_constants import USER_SESSION_ALGORITHM,  ACCESS_TOKEN_EXPIRE_MINUTES, DEFAUL_TOKEN_TYPE
from datetime import datetime, timedelta
import jwt
from configs.env import SECRET_KEY

def create_user_session(user_name):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_data = {"sub": user_name, "exp": datetime.utcnow() + access_token_expires}
    access_token = jwt.encode(access_token_data, SECRET_KEY, algorithm=USER_SESSION_ALGORITHM)
    token_type = DEFAUL_TOKEN_TYPE
    response = {"access_token": access_token, "token_type": token_type}
    return response