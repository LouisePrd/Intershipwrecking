from django.db import models

class Candidate(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Application(models.Model):
    company = models.CharField(max_length=200)
    description = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    type_of_application = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    link = models.URLField()
    def __str__(self):
        return self.company