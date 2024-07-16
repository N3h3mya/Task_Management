class Project:
    def __init__(self, id, name, description, tasks=None):
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks if tasks is not None else [] #List of tasks associated with the project
        
    def add_task(self, task):
        self.tasks.append(task)
        