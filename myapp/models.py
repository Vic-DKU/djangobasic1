from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=200)
    count = models.PositiveIntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.name
