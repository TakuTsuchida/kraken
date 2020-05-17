from models.auth.table import Auth

MESSAGE = []


async def is_registed(email: str) -> tuple:
    is_exist = await Auth.exists(email=email)
    if is_exist:
        MESSAGE.append("this email is already regested")
    return is_exist, MESSAGE


def is_normal(email: str, password: str) -> tuple:
    if not isinstance(email, str):
        MESSAGE.append("this email is not authorized")
        return False, MESSAGE
    if not isinstance(password, str):
        MESSAGE.append("this password is not authorized")
        return False, MESSAGE
    return True, MESSAGE


async def is_authorized(email: str, password: str) -> tuple:
    old_auth = await Auth.filter(email=email).first()
    is_authorized_email = email == old_auth.email
    if not is_authorized_email:
        MESSAGE.append("this email is wrong")
        return False, MESSAGE
    is_authorized_password = password == old_auth.password
    if not is_authorized_password:
        MESSAGE.append("this password is wrong")
        return False, MESSAGE
    return True, MESSAGE
