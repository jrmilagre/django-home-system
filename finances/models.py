from django.db import models

# Create your models here.
class Account(models.Model):
    account =models.CharField(max_length=60)

    def __str__(self):
        return self.account
