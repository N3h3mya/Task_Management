class Project:
    def __init__(self, id, name, description, tasks=None):
        self.id = id
        self.name = name
        self.description = description
        self.tasks = tasks if tasks is not None else []  # List of tasks associated with the project

    def add_task(self, task):
        self.tasks.append(task)  # Add a task to the project

    def remove_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]  # Create a new task list without the task with ID task_id
        
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task  # Go through all the tasks and return the one that matches the ID task_id
            
    def __str__(self):
        return f"Project({self.id}, '{self.name}', {len(self.tasks)} Tasks)"
