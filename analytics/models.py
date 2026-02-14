from django.db import models

class StudentRecord(models.Model):
    name = models.CharField(max_length=100)
    maths = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()
    computer = models.IntegerField()

    def total(self):
        return self.maths + self.science + self.english + self.computer

    def average(self):
        return self.total() / 4

    def __str__(self):
        return self.name
