from django.urls import path
from .views import dsaTracker, update_status, update_url

urlpatterns = [
    path('', dsaTracker, name='dsaTracker'),
    path('update_status/<int:id>/', update_status, name='update_status'),
    path('update_url/<int:id>/', update_url, name="question_update_url")
]