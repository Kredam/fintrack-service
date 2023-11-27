from django.urls import path
from .views import account_view

urlpatterns = [
    # name = easy to reference in view template
    path('', account_view),
]