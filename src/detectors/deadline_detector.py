def detect_deadline_conflicts(tasks):

  conflicts = []

  for task in tasks.values():
    end_time = task.start_time + task.duration

    if end_time > task.deadline: 
        conflicts.append(task)

  return conflicts
 