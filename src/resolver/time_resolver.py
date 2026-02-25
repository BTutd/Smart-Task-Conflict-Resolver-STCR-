
#Explaining Time Conflict

def explain_time_conflict(task1, task2):
    explanation = "Conflict Type: Time Overlap \n"

    explanation += f"Tasks Involved: {task1.id} and {task2.id}\n"
    explanation += "Explanation: \n"
    explanation += (
        f"Task {task1.id} run from {task1.start_time} to {task1.start_time + task1.duration} \n"
    )
    explanation += (
        f"Task {task2.id} run from {task2.start_time} to {task2.start_time + task2.duration}\n"
    )
    explanation += "These tasks overlap and cannot be done by the same owner.\n\n"

    return explanation

def suggest_time_fixes(task1,task2):
    return [
        f"Reschedule {task2.id} to start after {task1.id} finishes",
        f"Assign {task2.id} to a different owner",
        f"Reduce duration of one of the tasks",
    ]