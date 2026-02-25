def get_tasks_by_owner(owner, tasks):

    tasks_owner  = []

    for task in tasks.values():
        if  tasks_owner == owner:
            tasks_owner.append(task)
    
    return tasks_owner


