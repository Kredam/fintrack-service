from datetime import date
from .models import Account
from rest_framework.serializers import ModelSerializer, ValidationError

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def validate(self, attrs):
        if attrs['type'] == 'CRD' and len(attrs['number']) == 0:
            raise ValidationError({"number": _("Cards must have a number")}, code="required")
        if attrs['type'] == 'CSH' and len(attrs['number']) > 0:
            raise ValidationError({"number": _("Cash type has no accont number")}, code="invalid")
        return super().validate(attrs)