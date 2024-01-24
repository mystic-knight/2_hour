from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
import sentry_sdk
from database.db_session import db
from fastapi import FastAPI, Request
from configs.env import APP_ENV
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from services.user.user_router import user_router
from services.strategy.strategy_router import strategy_router
from time import time
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from services.user.user_params import Token
from services.user.interactions.authenticate_user import authenticate_user
# from services.user.firebase_code_logic import firebaseAdminAuth


docs = {
    "title": "Engines",
    "docs_url":  "/docs",
    "redoc_url": "/redoc",
    "openapi_url":  "/openapi.json",
    "debug": True,
    "swagger_ui_parameters": {"docExpansion": None},
}

app = FastAPI(**docs)

app.include_router(prefix = "/user", router=user_router, tags=['User Apis'])
app.include_router(prefix = "/strategy", router=strategy_router, tags=['Strategy Apis'])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/docs", include_in_schema=False)
# async def get_swagger_documentation(response: str = Depends(firebaseAdminAuth)):
#     return 


# @app.get("/redoc", include_in_schema=False)
# async def get_redoc_documentation(response: str = Depends(firebaseAdminAuth)):
#     return 

# @app.get("/openapi.json", include_in_schema=False)
# async def openapi(response: str = Depends(firebaseAdminAuth)):
#     return 



@app.middleware("http")
async def log_request_response_time(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.on_event("startup")
def startup():
    if db.is_closed():
        db.connect()


@app.on_event("shutdown")
def shutdown():
    if not db.is_closed():
        db.close()


@app.get("/", tags=["Health Checks"])
def read_root():
    return "Welcome To An Everything Engine"


@app.get("/user/health", tags=["Health Checks"])
def get_health_check():
    return JSONResponse(status_code=200, content={"status": "ok"})


@app.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    return authenticate_user(form_data.username,form_data.password)