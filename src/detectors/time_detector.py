#overlap Detector
def  detect_time_conflicts (tasks):
    
    conflicts = []

    task_list = list(tasks.values()) # to convert dict to list

    for i in range(len(task_list)):
        for j in range(i + 1,len(task_list)):
            t1 = task_list[i]
            t2 = task_list[j]

            #only check same owner
            if t1.owner != t2.owner:
                continue

            start1 = t1.start_time
            end1 = t1.start_time + t1.duration

            start2 = t2.start_time
            end2 = t2.start_time + t2.duration

            # check the overlap

            if start1 < end2 and start2 < end1:
                conflicts.append((t1,t2))
        
    return conflicts