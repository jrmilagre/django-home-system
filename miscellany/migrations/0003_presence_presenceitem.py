# Generated by Django 4.2.16 on 2024-11-17 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miscellany', '0002_justification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PresenceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=True)),
                ('justification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presences', to='miscellany.justification')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presences', to='miscellany.person')),
                ('presence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='miscellany.presence')),
            ],
        ),
    ]
