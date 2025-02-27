from django.db import models


class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    emojis = None

    def __str__(self):
        return self.content


from django.db import models

# Create your models here.
