from django.db.models import CASCADE, Q, TextChoices, UniqueConstraint, Model, ForeignKey, DateField, CharField, PositiveIntegerField, BigIntegerField, BooleanField
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.
class Expense(Model):

    class Types(TextChoices):
        YEARLY = 'YRLY', 'Yearly'
        MONTHLY = 'MNTH', 'Monthly'
        WEEKLY = 'WKLY', 'Weekly'


    name = CharField(null=False, blank=False)
    carvable = BooleanField(null=False, blank=False, default=False)
    planned_amount = PositiveIntegerField(null=True, blank=False)
    deduction_day = DateField(null=True, blank=False)
    type = CharField(choices=Types.choices, blank=False, null=False)
    account = ForeignKey('account.Account', on_delete=CASCADE)
    payed = BooleanField(null=True, blank=False, default=False)

    def clean(self) -> None:
        return super().clean()
    
class Transactions(Model):
    
    expense = ForeignKey(Expense, on_delete=CASCADE)
    name = CharField(null=False, blank=True)
    amount = PositiveIntegerField(null=False, blank=False)