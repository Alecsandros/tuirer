from django.db import models
from tuites.managers import TuitesManager

# Create your models here.

class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280) 
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField('users.User', blank=True)

    objects = TuitesManager()

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ('content', )