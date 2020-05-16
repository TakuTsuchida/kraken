from tortoise.models import Model
from tortoise import fields

class Auth(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, null=False)
    password = fields.CharField(max_length=100, null=False)
    # created = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# TODO separate validation
async def validate_is_exist(email: str) -> bool:
    is_exist = await Auth.exists(email=email)
    return is_exist

def validate_data(email: str, password: str) -> bool:
    if not isinstance(email, str):
        return False
    if not isinstance(password, str):
        return False
    return email and password

async def validate_password(email: str, password: str) -> bool:
    is_exist = await Auth.exists(email=email, password=password)
    print(email, password, is_exist, bool(is_exist))
    return is_exist

# TODO separate queries and commands
async def create(email: str, password: str) -> None:
    try:
        await Auth.create(email=email, password=password)
    except Exception as e:
        raise(e)
