from django.urls import path

from .views import index, deleteTransaction

urlpatterns = [
    path('', index, name="index"),
    path('/delete-trasaction/<uuid>', deleteTransaction, name="deleteTransaction")
]