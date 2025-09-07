from django.contrib import admin
from .models import Expense


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	list_display = ('expense_type', 'date', 'amount', 'quantity', 'created_at')
	search_fields = ('expense_type',)
	ordering = ('-date',)

