import responder
from tortoise import Tortoise
from routes.auth import auth_routes

api = responder.API()

@api.on_event("startup")
async def start_db_connection():
    await Tortoise.init(
        db_url="mysql://root:password@db:3306/docker_db",
        modules={"models": ["models.auth"]}
    )

@api.on_event("shutdown")
async def close_db_connection():
    await Tortoise.close_connections()

auth_routes(api)

if __name__ == '__main__':
    api.run(address='0.0.0.0',port=8082)
