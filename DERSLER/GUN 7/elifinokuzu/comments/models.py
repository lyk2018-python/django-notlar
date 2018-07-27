import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone

class Comment(models.Model):
    node = models.ForeignKey('dictionary.Node', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return str(self.node) + ": " + str(self.text)
