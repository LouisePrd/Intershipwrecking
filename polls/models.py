from django.db import models


class Application(models.Model):
    company = models.CharField(max_length=200)
    description = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
    type_of_application = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    link = models.URLField()