from src.resolver.deadline_resolver import explain_deadline_conflict, suggest_deadline_fixes
from src.resolver.dependency_resolver import explain_cycle, suggest_cycle_fixes
from src.resolver.time_resolver import explain_time_conflict, suggest_time_fixes
from src.detectors.analyzer import analyze_tasks
from src.utils.loader import load_tasks_from_json
from src.prioritizer.prioritizer import conflict_prioritizer
from src.scheduler.auto_shcedule import auto_scheduler

tasks = load_tasks_from_json("data/tasks.json")

results = analyze_tasks(tasks)
prioritized = conflict_prioritizer(results)

auto_scheduler(tasks, prioritized)


for conflict in prioritized:
    c_type = conflict["type"]
    t_ids = conflict["tasks"]
    print(f"\n Conflict Type: {c_type},Tasks:{t_ids},Priority:{conflict['priority']}\n")

    if c_type == "circular":
        fixes = suggest_cycle_fixes(t_ids)
    elif c_type == "time_overlap":
        t1,t2 = [tasks[t] for t in t_ids]
        fixes = suggest_time_fixes(t1,t2)
    elif c_type == "deadline":
        t = tasks[t_ids[0]]
        fixes = suggest_deadline_fixes(t)
    print("Suggested Fixes:")
    for i, fix in enumerate(fixes,1):
        print(f"{i}, {fix}")  