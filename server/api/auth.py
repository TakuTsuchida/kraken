from models.auth import validate_is_exist, validate_data, create

PAYLOADS = {}

async def signUp(req, resp):
    # moc data
    email = "test1@gmail.com" 
    password = "test1_pwd"

    # validation
    if await validate_is_exist(email):
        PAYLOADS["message"] = "already registration"
        resp.media = PAYLOADS
        resp.status_code = 400
        return
    if not validate_data(email, password):
        PAYLOADS["message"] = "bad data"
        resp.status_code = 400
        return

    # registration
    await create(email, password)
    resp.status_code = 201

def signIn(req, resp):
    resp.text = "world"
