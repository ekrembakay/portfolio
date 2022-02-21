from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.title