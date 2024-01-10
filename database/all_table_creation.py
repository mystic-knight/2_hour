from database.db_session import db
from services.user.models.user import User
from services.user.models.external_provider import ExternalProvider

def create_tables():
    try:
        all_tables = [ExternalProvider, User]
        db.create_tables(all_tables)
        db.close()
    except:
        print("Exception while creating table")
        raise
