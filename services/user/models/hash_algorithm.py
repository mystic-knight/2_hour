import datetime
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


class HashAlgorithm(BaseModel):
    id = UUIDField(primary_key=True, constraints=[SQL('DEFAULT gen_random_uuid()')])
    algorithm_name = TextField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now, null=True)
    updated_at = DateTimeField(default=datetime.datetime.now, null=True, index=True)

    class Meta:
        table_name = "hash_algorithms"

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(HashAlgorithm, self).save(*args, **kwargs)

    