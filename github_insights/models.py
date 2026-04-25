from django.db import models

class GitHubUser(models.Model):
    username = models.CharField(max_length=255, unique=True)
    data = models.JSONField()
    updated_at = models.DateTimeField(auto_now=True)