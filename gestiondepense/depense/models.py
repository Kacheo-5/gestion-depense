from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    expense_type = models.CharField(max_length=100, help_text="Exemple: Carburant, Huile, Réparation...")
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Quantité (litres) si applicable")
    amount = models.DecimalField(max_digits=12, decimal_places=2, help_text="Montant en FCFA")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.expense_type} - {self.amount} FCFA le {self.date}"
