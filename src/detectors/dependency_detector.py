
def detect_circular_dependencies(tasks):
    
    # Detects if there is a circular dependency among tasks.

    # Parameters:
    # - tasks: dict mapping task_id -> Task object

    # Returns:
    # - cycle_found: True if a cycle exists, False otherwise
    # - cycle_path: list of task_ids forming the cycle (empty if no cycle)
    
    
    visited = set()
    visiting = set()
    cycle_path = []

    def dfs(task_id,path):
        if task_id in visiting:
            cycle_path.extend(path[path.index(task_id):] + [task_id])
            return True
        if task_id in visited:
            return False
        
        visiting.add(task_id)
        path.append(task_id)

        for dep_id in tasks[task_id].dependencies:
            if dep_id not in tasks:
                continue
            if dfs(dep_id,path):
                return True
        
        visiting.remove(task_id)
        visited.add(task_id)
        path.pop()
        return False
    
    for task_id in tasks:
        if dfs(task_id, []):
            return True, cycle_path
        
    return False, []
