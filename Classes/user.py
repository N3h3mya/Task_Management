class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email
        
    def assign_task(self, task):
        task.assigned_to = self.id # Assigns a task to the user
        
    def __str__(self):
        return f"User({self.id}, '{self.username}', '{self.email}')"