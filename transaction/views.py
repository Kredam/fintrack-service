from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from .models import Transactions
from account.models import Account
from django.utils import timezone
from .serializers import TransactionSerializer
from rest_framework import status
from rest_framework.response import Response    

class TransactionViewSet(ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request: Request, *args, **kwargs):
        account_id = request.data['account']
        account: Account = Account.objects.get(id=account_id)
        account.balance -= request.data['amount'] 
        account.save()
        return super().create(request, *args, **kwargs)    

    def update(self, request: Request, *args, **kwargs):
        account_id = request.data['account']
        account: Account = Account.objects.get(id=account_id)
        account.balance = request.data['amount']
        account.save()
        return super().update(request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs):
        account_id = request.data['account']
        account: Account = Account.objects.get(id=account_id)
        account.balance += request.data['amount']
        account.save()
        return super().destroy(request, *args, **kwargs)

    @action(detail=False, methods=['GET'])
    def get_recent_transaction(self, request: Request):
        # 7 days, 14 days, 1 month
        days = int(request.GET.get("days"))
        date = timezone.now().date() - days
        queryset = Transactions.objects.filter(date__gte=date)
        serializer = TransactionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

