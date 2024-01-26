from .models import Transactions
from rest_framework.serializers import ModelSerializer

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'
