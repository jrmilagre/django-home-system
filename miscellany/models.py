from django.db import models


class Person(models.Model):

    full_name = models.CharField(max_length=60)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Justification(models.Model):

    justification = models.CharField(max_length=60)

    def __str__(self):
        return self.justification

class Presence(models.Model):
    presence_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Presença em {self.presence_date}"


class PresenceItem(models.Model):
    presence = models.ForeignKey(
        Presence,
        on_delete=models.CASCADE,
        related_name="items"  # Relaciona os itens com uma presença específica.
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="presences"  # Relaciona presenças com uma pessoa específica.
    )
    justification = models.ForeignKey(
        Justification,
        on_delete=models.SET_NULL,  # Permite que a justificativa seja nula.
        null=True,
        blank=True,
        related_name="presences"  # Relaciona presenças com uma justificativa específica.
    )

    def __str__(self):
        return f"{self.person} - {'Presente' if self.presence else 'Ausente'}"