from api.auth import (sign_up, sign_in)

BASE = "/auth"
SIGNUP = BASE + "/signUp"
SIGNIN = BASE + "/signIn"

def auth_routes(api):
    api.add_route(SIGNUP, sign_up)
    api.add_route(SIGNIN, sign_in)
