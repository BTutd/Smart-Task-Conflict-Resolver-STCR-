from src.detectors.deadline_detector import  detect_deadline_conflicts
from src.detectors.dependency_detector import detect_circular_dependencies
from src.detectors.time_detector import detect_time_conflicts


def analyze_tasks(tasks):
    results = {
        "Circular_dependencies": None,
        "Time_Conflict" : [],
        "Deadline_conflict": []
    }

    cycle_exists, cycle = detect_circular_dependencies(tasks)
    if cycle_exists:
        results["Circular_dependencies"] = cycle
    
    time_conflicts = detect_time_conflicts(tasks)
    results["Time_Conflict"] = time_conflicts

    deadline_conflicts =detect_deadline_conflicts(tasks)
    results["Deadline_conflict"]= deadline_conflicts

    return results

