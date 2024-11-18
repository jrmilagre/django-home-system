from django.contrib import admin

# Register your models here.
from .models import Person, Justification, Presence, PresenceItem


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(Justification)
class JustificationAdmin(admin.ModelAdmin):
    list_display = ['justification']


class PresenceItemInline(admin.TabularInline):
    model = PresenceItem
    extra = 0  # Evita mostrar linhas extras desnecessárias.



@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('presence_date',)
    inlines = [PresenceItemInline]  # Adiciona os itens diretamente no admin.
