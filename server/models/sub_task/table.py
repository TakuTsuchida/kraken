#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


class SubTask(Model):
    id = fields.IntField(pk=True)
    task = fields.ForeignKeyField('models.Task', related_name='sub_tasks')
    name = fields.CharField(max_length=100)
    describe = fields.TextField()
    deadline = fields.DatetimeField()
    status = fields.IntEnumField(Status)
    started_at = fields.DateField()
    ended_at = fields.DateField()
    created_at = fields.DateField()
    updated_at = fields.DateField()

    class Meta:
        table = "sub_task"


    def __str__(self):
        return self.name

