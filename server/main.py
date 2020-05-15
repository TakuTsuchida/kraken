import responder
from routes.auth import auth_routes

api = responder.API()
auth_routes(api)

if __name__ == '__main__':
    api.run(address='0.0.0.0',port=8082)