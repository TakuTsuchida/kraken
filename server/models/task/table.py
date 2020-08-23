from enum import IntEnum

from tortoise.models import Model
from tortoise import fields


class Status(IntEnum):
    yet = 1
    doing = 2
    done = 3


class Task(Model):
    id = fields.IntField(pk=True)
    auth = fields.ForeignKeyField('models.Auth', related_name='task', to_field="id")
    name = fields.CharField(max_length=100)
    description = fields.TextField()
    deadline = fields.DateField()
    importance = fields.IntField()
    status = fields.IntEnumField(Status)
    started_at = fields.DateField(null=True)
    ended_at = fields.DateField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "task"

    def __str__(self):
        return self.name
