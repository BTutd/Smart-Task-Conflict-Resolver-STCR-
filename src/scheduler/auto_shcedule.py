def auto_scheduler(tasks, prioritized):
    for conflict in prioritized:
        if conflict["type"] == "time_overlap":
            print(conflict)