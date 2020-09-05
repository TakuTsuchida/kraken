async def get_auth(req):
    from blogic.auth import decode_token
    from models.auth.interface import get as auth_get

    if not req.session.get("token"):
        resp.status_code = 500
        return None, False
    email = decode_token(req.session["token"])["email"]
    return await auth_get(email), True
