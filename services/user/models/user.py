import datetime
from peewee import (
    UUIDField,
    SQL,
    BooleanField,
    Model,
    TextField,
    DateTimeField,
    CharField,
    ForeignKeyField
)
from database.db_session import db
from pydantic import EmailStr, Field
from services.user.models.external_provider import ExternalProvider
from passlib.context import CryptContext

pwd_context  = CryptContext(schemes = ['bcrypt'], deprecated="auto")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = UUIDField(constraints=[SQL('DEFAULT gen_random_uuid()')], primary_key=True)
    user_name = CharField(index = True)
    email = CharField(index = True)
    password_digest = TextField(index = True)
    mobile_number = TextField(index = True, null = True)
    mobile_country_code = TextField(index = True, null = True)
    mobile_verified = BooleanField(default=False, index = True)
    password_salt = TextField(index = True,  null=True)
    email_confirmation_token = TextField(index = True, null = True)
    email_validation_status = BooleanField(default=False, index = True)
    external_provider_id = ForeignKeyField(ExternalProvider, backref='external_provider_id', null = True)
    external_provider_token = TextField(index = True, null=True)
    google_id = CharField(unique=True, null=True)
    source = TextField(default="active", index=True, null=False)
    created_at = DateTimeField(default=datetime.datetime.now, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now, null=True, index=True)
    
    class Meta:
        table_name = "users"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)
    
    def set_password(self, password):
        self.password_digest = pwd_context.hash(password)
    
    def verify_password(self, plain_password, password_digest):
        verify = pwd_context.verify(plain_password, password_digest)
        return verify

    