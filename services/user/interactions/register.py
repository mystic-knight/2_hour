from services.user.models.user import User
from services.user.interactions.create_user_session import create_user_session


def register(request):
    response = {"success": True, "status_code": 200}
    uniques_user = User.select().where(User.user_name == request.user_name).first()
    if not uniques_user:
        uniques_user = User(user_name=request.user_name)
    
    uniques_user.set_password(request.password)
    uniques_user.status = 'active'
    uniques_user.email = request.email
    uniques_user.save()
    response['id'] = str(uniques_user.id)
    session_response = create_user_session(request.user_name)
    response['access_token'] = session_response['access_token']
    response['token_type'] = session_response['token_type']

    return response
