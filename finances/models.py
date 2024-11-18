from django.db import models

# My models.


class Account(models.Model):

    account = models.CharField(max_length=60)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    opening_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.account

class Movement(models.Model):

    buy_date = models.DateField(null=True, blank=True)
    movement_date = models.DateField(null=True, blank=True)
    value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,  # Exclui os movimentos ao excluir a conta.
        related_name='movements',  # Permite acessar os movimentos de uma conta com account.movements.all().
        null=True,  # Opcional, permite valores nulos ao criar novos movimentos.
        blank=True,  # Opcional nos formulários.
    )

    def __str__(self):
        return f"Movement on {self.movement_date} - Value: {self.value}"