from api.task import task_create, task_list

BASE = "/task"
NEW = BASE + "/new"
LIST = BASE + "/list"

def task_routes(api):
    api.add_route(NEW, task_create)
    api.add_route(LIST, task_list)
