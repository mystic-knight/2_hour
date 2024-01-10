from services.user.models.user import User
from fastapi import HTTPException
from services.user.interactions.create_user_session import create_user_session



def authenticate_user(user_name, password):
    response = {"success": False, "status_code": 400}
    user = User.select().where(User.user_name == user_name).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    verification = user.verify_password(password, user.password_digest)
    response['success'] = True
    response['status_code'] = 200
    response['user_verified'] = verification
    session_response = create_user_session(user.user_name)
    response['access_token'] = session_response['access_token']
    response['token_type'] = session_response['token_type']
    return response

