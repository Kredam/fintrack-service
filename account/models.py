from django.db import models
from django.conf import settings

# Create your models here.
class Account(models.Model):
   
    class Types(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CREDIT_CARD = 'CCARD', 'Credit card'
        DEBIT_CARD = 'DCARD', 'Debit card'

    expire = models.DateField(null=True)
    type = models.CharField(choices=Types.choices, null=False)
    number = models.BigIntegerField(null=True, max_length=19)
    balance = models.BigIntegerField(null=False, blank=False, default=0)
    description = models.CharField(null=False, blank=True)
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
