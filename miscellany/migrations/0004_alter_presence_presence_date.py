# Generated by Django 4.2.16 on 2024-11-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miscellany', '0003_presence_presenceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presence',
            name='presence_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
