from django.db import models

class Intern(models.Model):
    name=models.CharField(max_length=20)
    Domain=models.CharField(max_length=20)
    stipend=models.PositiveIntegerField()
    def __str__(self):
        return self.name