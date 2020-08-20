RESP_DATA = {}

async def new(req, resp):
    from models.task.interface import create as task_create
    from models.auth.interface import get as auth_get
    from blogic.auth import decode_token

    # bind
    if not req.session.get("token"):
        resp.status_code = 500
        return
    email = decode_token(req.session["token"])["email"]
    auth_model = await auth_get(email)

    data = await req.media()
    title = data["title"]
    description = data["description"]
    deadline = data["deadline"]
    importance = data["importance"]

    # registration
    is_ok, message = await task_create(title=title,
                                       auth_id=auth_model.id,
                                       description=description,
                                       deadline=deadline,
                                       importance=importance)
    if not is_ok:
        RESP_DATA["message"] = message
        resp.media = RESP_DATA
        resp.status_code = 400
        return
    resp.status_code = 201
