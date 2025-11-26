from django.urls import path
from .views import dsaTracker, update_status

urlpatterns = [
    path('', dsaTracker, name='dsaTracker'),
    path('/update_status/<id>', update_status, name='update_status')
]