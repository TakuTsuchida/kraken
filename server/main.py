import responder
import uvicorn
from tortoise import Tortoise
from routes.auth import auth_routes
from routes.task import task_routes

api = responder.API()

@api.on_event("startup")
async def start_db_connection():
    await Tortoise.init(
        db_url="mysql://root:password@db:3306/docker_db",
        modules={"models": ["models.auth.table", "models.task.table"]}
    )

@api.on_event("shutdown")
async def close_db_connection():
    await Tortoise.close_connections()

auth_routes(api)
task_routes(api)

if __name__ == '__main__':
    uvicorn.run("main:api", host="0.0.0.0", port=8082, reload=True, log_level="info")
