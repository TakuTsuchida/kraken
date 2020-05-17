from models.auth.table import Auth

from models.auth.validation import is_registed, is_normal

async def create(email: str, password: str) -> tuple:
    is_ok, message = is_normal(email, password)
    if not is_ok:
        return False, message
    is_no, message = await is_registed(email)
    if is_no:
        return False, message
    try:
        await Auth.create(email=email, password=password)
    except Exception as e:
        raise(e)
    return True, None
