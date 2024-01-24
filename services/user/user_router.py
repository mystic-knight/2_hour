
from fastapi import Depends, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from services.user.user_params import *
from services.user.interactions.register import register
from services.user.interactions.authenticate_user import authenticate_user
from services.user.interactions.get_current_user import get_current_user
from services.user.interactions.check_user_name import check_user_name
from services.user.interactions.request_otp import request_otp
from services.user.models.user import User
import requests
from jose import jwt

# should be in a seprate file
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
GOOGLE_CLIENT_ID = "333736231292-mi3e9gkn4br1dgtfuu0raflci7jghlrv.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
FRONTEND_URL =  'http://127.0.0.1:8000'


config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
import google_auth_oauthlib.flow
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'test.json',
    scopes=['https://www.googleapis.com/auth/drive'])
flow.redirect_uri = FRONTEND_URL

user_router = APIRouter()



@user_router.post('/register')
def register_api(request: RegisterUser):
    try:
        return register(request)
    except HTTPException as e:
        raise
    except Exception as e:
        # raise in sentry as well
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )

@user_router.get('/login')
def login_api(
    user_name: str,
    password: str,
):
    try:
        return authenticate_user(user_name, password)
    except HTTPException as e:
        raise
    except Exception as e:
        # raise in sentry as well
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )

@user_router.get('/check_user_name')
def login_api(
    user_name: str,
):
    try:
        return check_user_name(user_name)
    except HTTPException as e:
        raise
    except Exception as e:
        # raise in sentry as well
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )



@user_router.get('/protected')
async def get_current_active_user_api(
    current_user: str = Depends(get_current_user),
):
    try:
        return {"message": "This is a protected route", "current_user": current_user}
    except HTTPException as e:
        raise
    except Exception as e:
        # raise in sentry as well
        return JSONResponse(
            status_code=500, content={"success": False, "error": str(e)}
        )

@user_router.get('/send_otp')
def send_otp_via_twilio(to_phone_number: str):
    return request_otp(to_phone_number)




@user_router.get("/login/google")
async def login_google():
    authorization_url, state = flow.authorization_url(access_type='offline',include_granted_scopes='true')
    return {
        "url": authorization_url
    }


@user_router.get("/auth/google")
async def auth_google(code: str):
    token_url = "https://accounts.google.com/o/oauth2/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": FRONTEND_URL,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    return user_info.json()



@user_router.get("/token")
async def get_token(token: str = Depends(oauth2_scheme)):
    return jwt.decode(token, GOOGLE_CLIENT_SECRET, algorithms=["HS256"])
