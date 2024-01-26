from django.db.models import CASCADE, Q, TextChoices, UniqueConstraint, Model, ForeignKey, DateField, CharField, PositiveIntegerField, BigIntegerField
from django.conf import settings
from django.core.exceptions import ValidationError
import calendar

# Create your models here.
class Account(Model):

    class Types(TextChoices):
        CASH = 'CSH', 'Cash'
        CREDIT_CARD = 'CRD', 'Card'

    expire = DateField(null=True)
    type = CharField(choices=Types.choices, null=False, max_length=4)
    number = PositiveIntegerField(null=True, max_length=19)
    balance = BigIntegerField(null=False, blank=False, default=0)
    description = CharField(null=False, blank=True, max_length=100)
    holder = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                condition=Q(type='CRD'),
                fields=['number', 'holder'],
                name='unique-card'
            )
        ]

    def clean(self) -> None:
        if hasattr(self, "number") is False and self.type == 'CRD':
            raise ValidationError({"number": "Cards must have a number"}, code="required")
        if hasattr(self, "number") and self.type == 'CSH':
            raise ValidationError({"number": "Cash type has no account number"}, code="invalid")
        return super().clean()