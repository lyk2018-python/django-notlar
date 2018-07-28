from django.db import models

class Issue(models.Model):
    url = models.CharField(max_length=255)
    explantation = models.TextField(max_length=2000)

    def __str__(self):
        return self.url