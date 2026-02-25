def conflict_prioritizer (results):


    conflict_with_prioritizer = []

    # circular
    if results["Circular_dependencies"]:
        conflict_with_prioritizer.append(
            {"type": "circular","tasks": results["Circular_dependencies"],"priority":3}
        )
    # time
    for t1,t2 in results["Time_Conflict"]:
        conflict_with_prioritizer.append(
            {"type": "time_overlap","tasks": [t1.id, t2.id],"priority":2}
        )
    # deadline
    for task in results["Deadline_conflict"]:
        conflict_with_prioritizer.append(
            {"type":"Deadline_conflict","tasks": [task.id],"priority": 1}
        )
    # sort descending-> highest to lowest sorting
    conflict_with_prioritizer.sort(key=lambda x: x["priority"],reverse=True)

    return conflict_with_prioritizer
