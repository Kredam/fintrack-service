from django.urls import path
from .views import TransactionViewSet

urlpatterns = [
    path('<int:pk>', TransactionViewSet.as_view({'get': 'retrieve'})),
    path('all', TransactionViewSet.as_view({'get': 'list'})),
    path('create', TransactionViewSet.as_view({'post': 'create'}))
]