from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
class Expense(models.Model):

    class RecurrenceTypes(models.TextChoices):
        YEARLY = 'YRLY', 'Yearly'
        MONTHLY = 'MNTH', 'Monthly'
        WEEKLY = 'WKLY', 'Weekly'

    class ExpenseType(models.TextChoices):
        GROCERIES = 'GRCRS', 'Groceries'
        UTILITIES = 'UTLTS', 'Utilities'
        HEALTH = 'HLTH', 'Health'
        TRANSPORT = 'TRNPRT', 'Transport'
        HOME = 'HOME', 'Home'
        CLOTHING = 'CLTH', 'Clothing'
        DEBT = 'DBT', 'Debt'
        GAS = 'GS', 'Gas'
        OTHER = 'OTHR', 'Other'

    type = models.CharField(choices=ExpenseType.choices, max_length=6, default=ExpenseType.OTHER)
    account = models.ForeignKey('account.Account', on_delete=models.SET_NULL, null=True)
    carvable = models.BooleanField(null=False, blank=False, default=False)
    amount = models.PositiveIntegerField(null=False, blank=False, default=0)
    period_start = models.DateField(null=True, blank=False)
    period_end = models.DateField(null=True, blank=False)
    recurrence_type = models.CharField(choices=RecurrenceTypes.choices, default=RecurrenceTypes.MONTHLY)

    def clean(self) -> None:
        return super().clean()