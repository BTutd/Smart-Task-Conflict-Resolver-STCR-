class Task :
    """
    Represents a single task in the STCR system.

    Fields:
    - id: Unique identifier for the task
    - name: Human-readable name of the task
    - owner: Who is responsible for this task
    - start_time: Proposed start time (integer, e.g., hour index)
    - duration: Duration of the task in hours (must be > 0)
    - deadline: Latest time the task must finish
    - dependencies: List of task IDs that this task depends on
    """

    def __init__(self,id,name,owner,start_time,duration,deadline,dependencies=None):
        self.id = id
        self.name = name
        self.owner = owner
        self.start_time = start_time
        self.duration = duration
        self.deadline = deadline
        self.dependencies = dependencies if dependencies else []
    
    def __repr__(self):
        return f"Task({self.id},{self.name},{self.owner})"