from django.db import models

# Create your models here.
# Create your models here.
class Income(models.Model):

    class Types(models.TextChoices):
        YEARLY = 'YRLY', 'Yearly'
        MONTHLY = 'MNTH', 'Monthly'
        WEEKLY = 'WKLY', 'Weekly'

    name = models.CharField(null=False, blank=False)
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(null=True, blank=False)
    period_start = models.DateField(null=True, blank=False)
    period_end = models.DateField(null=True, blank=False)
    type = models.CharField(choices=Types.choices, blank=False, null=False)

    def clean(self) -> None:
        return super().clean()
    