RESP_DATA = {}

async def signUp(req, resp):
    from models.auth.interface import create as auth_create

    # bind
    data = await req.media()
    email = data["email"]
    password = data["password"]

    # registration
    is_ok, message = await auth_create(email, password)
    if not is_ok:
        RESP_DATA["message"] = message
        resp.media = RESP_DATA
        resp.status_code = 400
        return
    resp.status_code = 201

async def signIn(req, resp):
    from models.auth.validation import is_authorized as validation_is_authorized
    from blogic.auth import create_token

    # bind
    data = await req.media()
    email = data["email"]
    password = data["password"]

    # signin check
    is_ok, message = await validation_is_authorized(email, password)
    if not is_ok:
        RESP_DATA["message"] = message
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
