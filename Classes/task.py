class Task:
    def __init__(self, id, title, description, due_date, status, assigned_to):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date #ending date of the task
        self.status = status
        self.assigneed_to = assigned_to #id of the user who is assigned to the task