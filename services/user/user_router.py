
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



