from api.auth import (signUp, signIn)

BASE = "/auth"
SIGNUP = BASE + "/signUp"
SIGNIN = BASE + "/signIn"

def auth_routes(api):
    api.add_route(SIGNUP, signUp)
    api.add_route(SIGNIN, signIn)
