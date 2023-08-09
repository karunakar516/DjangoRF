
# Create your models here.
from django.db import models
class Cricketer(models.Model):
    name=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    MatchesPlayed=models.PositiveIntegerField()
    def __str__(self):
        return self.name