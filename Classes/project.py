class Project:
    def __init__(self, id, name, description, tasks=None):
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks if tasks is not None else [] #List of tasks associated with the project
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, task):
        self.tasks = [task for task in self.tasks if task.id != task.id] #Creates a new task list that does not contain the task with the ID task_id
        
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task  #Goes through all the tasks and returns the one with the ID that matches task_id.

    def __str__(self):
                return f"Project({self.id}, '{self.name}', {len(self.tasks)} Tasks)"
