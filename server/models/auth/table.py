from tortoise.models import Model
from tortoise import fields

class Auth(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, null=False)
    password = fields.CharField(max_length=100, null=False)
    # created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.email
