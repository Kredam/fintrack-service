from django.urls import path
from .views import account_view

urlpatterns = [
    # name = easy to reference in view template
    path('detail/<int:pk>/', account_view),
    path('detail', account_view)
]