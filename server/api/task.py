RESP_DATA = {}

async def task_create(req, resp):
    from models.task.interface import create as task_create
    from api.common import get_auth

    # auth
    auth_model, ok = await get_auth(req)
    if not ok:
        return

    # bind
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

async def task_list(req, resp):
    from api.common import get_auth
    from models.task.interface import get_by
    from lib.date import date2str

    # auth
    auth_model, ok = await get_auth(req)
    if not ok:
        return

    # get tasks
    task_models = await get_by(auth_id=auth_model.id)
    RESP_DATA["tasks"] = list(map(lambda t: {"id": t.id,
                                             "title": t.name,
                                             "description": t.description,
                                             "deadline": date2str(t.deadline),
                                             "importance": t.importance,
                                             "status": t.status,
                                             "started_at": t.started_at,
                                             "ended_at": t.ended_at}, task_models))
    resp.media = RESP_DATA
    resp.status_code = 200