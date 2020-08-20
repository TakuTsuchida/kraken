from api.task import (new)

BASE = "/task"
NEW = BASE + "/new"

def task_routes(api):
    api.add_route(NEW, new)
