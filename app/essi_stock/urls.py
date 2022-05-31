from django.urls import path
from .api_views import Stock

urlpatterns = [
    path('api/', Stock.as_view()),
]