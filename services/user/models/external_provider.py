import uuid, datetime, json, re
from peewee import (
    UUIDField,
    SQL,
    Model,
    DateTimeField,
    TextField
)
from database.db_session import db


class BaseModel(Model):
    class Meta:
        database = db


class ExternalProvider(BaseModel):
    id = UUIDField(primary_key=True, constraints=[SQL('DEFAULT gen_random_uuid()')])
    provider_name = TextField(null=True, index = True)
    ws_endpoint = TextField(null=True, index = True)
    created_at = DateTimeField(default=datetime.datetime.now, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now, null=True, index=True)

    class Meta:
        table_name = "external_providers"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(ExternalProvider, self).save(*args, **kwargs)

    