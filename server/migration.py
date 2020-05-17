from tortoise import Tortoise, run_async

async def migrate():
    await Tortoise.init(
        db_url="mysql://root:password@db:3306/docker_db",
        modules={
            "models": [
                "models.auth.table"
            ]
        }
    )
    await Tortoise.generate_schemas()

    print("Success migration!!")

run_async(migrate())