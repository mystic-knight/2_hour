import uuid, datetime, json, re
from peewee import (
    UUIDField,
    SQL,
    BooleanField,
    Model,
    DateTimeField,
)
from database.db_session import db


class BaseModel(Model):
    class Meta:
        database = db


class EmailValidationStatus(BaseModel):
    id = UUIDField(primary_key=True, constraints=[SQL('DEFAULT gen_random_uuid()')])
    status = BooleanField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now, null=True, index=True)

    class Meta:
        table_name = "hash_algorithms"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(EmailValidationStatus, self).save(*args, **kwargs)

    