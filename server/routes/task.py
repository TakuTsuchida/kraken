from api.task import task_create, task_delete, task_list

BASE = "/task"
NEW = BASE + "/new"
DELETE = BASE +"/delete/{id}"
LIST = BASE + "/list"

def task_routes(api):
    api.add_route(NEW, task_create)
    api.add_route(DELETE, task_delete)
    api.add_route(LIST, task_list)
