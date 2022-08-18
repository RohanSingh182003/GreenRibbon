from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.TextField()
    email = models.EmailField()
    childs_name = models.TextField()
    relationship = models.CharField(max_length=50)
    childs_age = models.IntegerField()

    def __str__(self):
        return self.name

class Psychomotor(models.Model):
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    q5 = models.TextField()

class Psychomotor1(models.Model):
    q6 = models.TextField()
    q7 = models.TextField()
    q8 = models.TextField()
    q9a = models.TextField()
    q9b = models.TextField()
    q9c = models.TextField()
    q10a = models.TextField()
    q10b = models.TextField()
    q10c = models.TextField()

class Psychomotor2(models.Model):
    q11a = models.TextField()
    q11b = models.TextField()
    q11c = models.TextField()
    q12a = models.TextField()
    q12b = models.TextField()
    q12c = models.TextField()
    q13a = models.TextField()
    q13b = models.TextField()
    q13c = models.TextField()
    q14a = models.TextField()
    q14b = models.TextField()
    q14c = models.TextField()

class Cognitive(models.Model):
    q1 = models.TextField()
    q2 = models.TextField()
    q3 = models.TextField()
    q4 = models.TextField()
    q5 = models.TextField()
    q6 = models.TextField()

class Cognitive1(models.Model):
    q7 = models.TextField()
    q8 = models.TextField()
    q9 = models.TextField()
    q10 = models.TextField()
    q11 = models.TextField()
