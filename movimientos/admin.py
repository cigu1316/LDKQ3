from django.contrib import admin
from movimientos.models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):  
    list_display = ('date','descriptions', 'income', 'expenses','balance','totall')
    