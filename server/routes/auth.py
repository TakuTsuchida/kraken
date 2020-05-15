from api.auth import *

BASE = "/auth"
SIGNUP = BASE + "/signup"
SIGNIN = BASE + "/signin"

def auth_routes(api):
    api.add_route(SIGNUP, signup)
    api.add_route(SIGNIN, signin)
