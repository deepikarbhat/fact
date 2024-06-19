

from django.urls import path
from .views import calculate_factorials

urlpatterns = [
    path('factorials/', calculate_factorials, name='factorials'),
]
