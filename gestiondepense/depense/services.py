from django.db import transaction
from .models import Expense


def list_expenses():
    return Expense.objects.all()


def get_expense(pk):
    return Expense.objects.filter(pk=pk).first()


@transaction.atomic
def create_expense(validated_data):
    return Expense.objects.create(**validated_data)


@transaction.atomic
def update_expense(instance, validated_data):
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()
    return instance


@transaction.atomic
def delete_expense(instance):
    instance.delete()
