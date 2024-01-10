from services.user.models.user import User

def check_user_name(user_name):
    response = {"success": True, "status_code": 200, "user_present": False}
    check = User.select().where(User.user_name == user_name).first()
    if check:
        response['user_present'] = True
        return response
    
    return response
    
