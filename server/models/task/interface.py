from models.task.table import Task

STATUS = {
    "yet": 1,
    "doing": 2,
    "done": 3}


async def create(title: str, auth_id: int, description: str, deadline: str, importance: int) -> tuple:
    try:
        await Task.create(name=title,
                          auth_id=auth_id,
                          description=description,
                          deadline=deadline,
                          importance=importance,
                          status=STATUS["yet"])
    except Exception as e:
        raise(e)
    return True, None

async def get_by(**kwargs):
    return await Task.filter(**kwargs, ).order_by("deadline", "-importance")
