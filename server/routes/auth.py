from api.auth import *

BASE_URL = "/auth"
SIGNUP = BASE_URL + "/signup"
SIGNIN = BASE_URL + "/signin"

def auth_routes(api):
    api.add_route(SIGNUP, signup)
    api.add_route(SIGNIN, signin)
