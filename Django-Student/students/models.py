from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    sap = models.CharField(max_length=15, default='60017220086')
    age = models.IntegerField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.name
