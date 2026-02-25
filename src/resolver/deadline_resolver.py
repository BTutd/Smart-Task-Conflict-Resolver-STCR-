# explain the deadline coflict

def explain_deadline_conflict(task):
    explanation = "Conflict Type: Deadline Violation\n"
    explanation +=  f"Task Involved: {task.id} \n"

    explanation += "Expalanation: \n"
    explanation += (
        f"Task {task.id} starts at {task.start_time} and takes {task.duration} hours.\n"
    )
    explanation += (
        f"It finishes at {task.start_time + task.duration}, but the deadline is {task.deadline}.\n"
    )
    explanation += "This task cannot be completed before its deadline!! \n"

    return explanation

def  suggest_deadline_fixes(task):
    return [
        f"Start {task.id} earlier",
        f"Reduce duration of {task.id}",
        f"Extend the deadline of {task.id}"
    ]