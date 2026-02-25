from models.task import Task
from detectors.analyzer import detect_circular_dependencies

tasks = {
    "A": Task("A", "Task A", "User1", 9,2,12, ["B"]),
    "B": Task("B", "Task B", "User2", 10,3,14, ["C"]),
    "C": Task("C", "Task C", "User1", 11,1,13, ["A"]),


}
cycle_exists, cycle = detect_circular_dependencies(tasks)
print("Cycle exists?", cycle_exists)
print("Cycle path:", cycle)
