from models.auth import (validate_is_exist, validate_data, create, validate_password)
from blogic.auth import create_token

RESP_DATA = {}

async def signUp(req, resp):
    # bind
    data = await req.media()
    email = data["email"]
    password = data["password"]

    # validation
    if not validate_data(email, password):
        RESP_DATA["message"] = "bad data"
        resp.status_code = 400
        return
    if await validate_is_exist(email):
        RESP_DATA["message"] = "already registration"
        resp.media = RESP_DATA
        resp.status_code = 400
        return

    # registration
    await create(email, password)
    resp.status_code = 201

async def signIn(req, resp):
    # bind
    data = await req.media()
    email = data["email"]
    password = data["password"]

    # validation
    if not await validate_is_exist(email):
        RESP_DATA["message"] = "incorrect email"
        resp.media = RESP_DATA
        resp.status_code = 400
        return
    if not await validate_password(email, password):
        RESP_DATA["message"] = "incorrect passoword"
        resp.media = RESP_DATA
        resp.status_code = 400
        return

    # get token
    token = create_token(email)
    RESP_DATA["email"] = email
    RESP_DATA["password"] = password
    RESP_DATA["token"] = token
    resp.media = RESP_DATA
    resp.status_code = 200
