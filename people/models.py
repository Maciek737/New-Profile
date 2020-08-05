from django.db import models

class Profile(models.Model):
    name = models.TextField(max_length=200)
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name