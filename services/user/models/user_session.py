import datetime
from peewee import (
    UUIDField,
    SQL,
    BooleanField,
    Model,
    DateTimeField,
    CharField,
    ForeignKeyField
)
from database.db_session import db
from services.user.models.user import User


class BaseModel(Model):
    class Meta:
        database = db


class UserSession(BaseModel):
    id = UUIDField(primary_key=True, constraints=[SQL('GENERATE gen_random_uuid()')])
    user_id = ForeignKeyField(User, backref='user_id')
    auth_scope = CharField(index = True)
    status = BooleanField(default=False, index=True)
    auth_mode = CharField(index = True)
    expire_at = DateTimeField(default=datetime.datetime.now + datetime.timedelta(30), null=True)
    platform = CharField(default = 'app')
    auth_device = CharField(default = 'desktop')
    created_at = DateTimeField(default=datetime.datetime.now, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now, null=True, index=True)

    class Meta:
        table_name = "user_sessions"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(UserSession, self).save(*args, **kwargs)

    