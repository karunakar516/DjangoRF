from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=15)
    fathername=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    def __str__(self):
        return self.name