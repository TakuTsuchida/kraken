from enum import IntEnum

from tortoise.models import Model
from tortoise import fields


class Importance(IntEnum):
    low = 1
    mid = 2
    high = 3

class Status(IntEnum):
    yet = 1
    doing = 2
    done = 3

class Task(Model):
    id = fields.IntField(pk=True)
    auth = fields.ForeignKeyField('models.Auth', related_name='tasks')
    name = fields.TextField()
    deadline = fields.DatetimeField()
    importance = fields.IntEnumField(Importance)
    status = fields.IntEnumField(Status)

    def __str__(self):
        return self.name

