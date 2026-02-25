def explain_cycle(cycle_path, tasks):
    if not cycle_path:
        return "No circular depedency found"
    
    explanation = "Conflict type: circulart dependency \n\n"

    # show path
    path_str = " -> ".join(cycle_path)
    explanation += f"Task Involved: {path_str} \n\n"

    #explain logic
    explanation += "Explanation:\n"
    for i in range(len(cycle_path) - 1):
        current = cycle_path[i]
        next_task = cycle_path[i+1]
        explanation += f"task {current} dependes on {next_task} \n"
    
    explanation += "this creates a loop where no task can start.\n\n"

    return explanation

def suggest_cycle_fixes(cycle_path):
    fixes = []

    for i in range(len(cycle_path) - 1):
        a = cycle_path[i]
        b = cycle_path[i+1]
        fixes.append(f"remove the dependency {a} -> {b}")

    return fixes
