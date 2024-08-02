# api/models.py
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    roll_number = models.CharField(max_length=20)

    def user_id(self):
        return f"{self.full_name.lower().replace(' ', '_')}_{self.dob.strftime('%d%m%Y')}"

