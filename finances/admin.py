from django.contrib import admin

# Register your models here.
from .models import Account, Movement


class AccountAdmin(admin.ModelAdmin):
    list_display = ['account', 'opening_balance', 'opening_date']


class MovementAdmin(admin.ModelAdmin):
    list_display = ['buy_date', 'movement_date', 'value', 'account']


admin.site.register(Account, AccountAdmin)
admin.site.register(Movement, MovementAdmin)
