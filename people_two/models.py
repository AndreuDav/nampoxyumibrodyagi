from datetime import datetime
from types import new_class

from django.db import models

class Status():
    new = 'new'
    in_progress = 'in_progress'
    done = 'done'

class Task():
    def __init__(self, id, project, description, status, assigne, created_at, updated_at):
        self.id = id
        self.project = project
        self.description = description
        self.status = status
        self.assigne = assigne
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def update_status(self, status):
        if isinstance(status, Status):
            self.status = status
            self.updated_at = datetime.now()

    def __str__(self):
        return f'task:{self.id}(title:{self.title}, status:{self.status}, assigne:{self.assigne})'

