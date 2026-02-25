import json 
from src.models.task import Task

def load_tasks_from_json(file_path):
    # read task from json file and convert them into task objects

    with open(file_path,"r") as file:
        data = json.load(file)
    tasks ={}

    for t in data["tasks"]:
        validate_task_data(t)
        task = Task(
            id=t["id"],
            name=t["name"],
            owner=t["owner"],
            start_time=t["start_time"],
            duration=t["duration"],
            deadline=t["deadline"],
            dependencies=t.get("dependencies",[])
        )
        tasks[task.id] = task

    return tasks

# add validation if the json goes wrong
def validate_task_data(task):
    required_fields = ["id", "name", "owner", "start_time", "duration", "deadline"]

    for field in required_fields:
        if field not in task:
            raise ValueError(f"Missing field: {field}")

    if task["duration"] <= 0:
        raise ValueError(f"Invalid duration in task {task['id']}")
