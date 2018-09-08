from django.db import models
from tuites.managers import TuitesManager
from users.models import User

# Create your models here.

class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280) 
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)

    objects = TuitesManager()

    @property
    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ('content', )