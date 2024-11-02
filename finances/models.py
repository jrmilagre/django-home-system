from django.db import models

# My models.
class Account(models.Model):
    account =models.CharField(max_length=60)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return self.account
