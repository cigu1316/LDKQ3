from django.contrib import admin
from movimientos.models import Register

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):  
    list_display = ('descriptions', 'income', 'expenses', 'balance', 'date')
    list_filter = ('descriptions', 'income', 'expenses', 'balance', 'date')
    search_fields = ('descriptions', 'income', 'expenses', 'balance', 'date')
    date_hierarchy = 'date'
    ordering = ('date',)
