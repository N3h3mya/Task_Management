class Notification:
    def __init__(self, id, user_id, message):
        self.id = id
        self.user_id = user_id
        self.message = message
        
    def send_notification(self):
        print(f"Notification pour l'utilisateur {self.user_id}: {self.message}")
        
    def __str__(self):
        return f"Notification({self.id}, User: {self.user_id}, Message: '{self.message}')"