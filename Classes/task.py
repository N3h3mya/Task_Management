class Task:
    def __init__(self, id, title, description, due_date, status, assigned_to):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date #ending date of the task
        self.status = status
        self.assigneed_to = assigned_to #id of the user who is assigned to the task
        
def update_status(self, new_status):
    self.status = new_status
    
#Converted the Task object to a dictionary for json storage    
def to_json(self):
    return {
        'id' : self.id,
        'title': self.title,
        'description': self.description,
        'due_date': self.due_date,
        'status': self.status,
        'assigned_to': self.assigned_to
        
    }