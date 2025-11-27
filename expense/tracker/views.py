from django.db.models import Sum
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transactions

# Create your views here.

def index(request):
    if request.method == "POST":
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        
        if description is None:
            messages.info(request, "Please enter description")
            return redirect('/')

        try :
            amount = float(amount)
        except ValueError:
            messages.info(request, "Please enter valid amount")
            return redirect('/')

        # saving transaction
        Transactions.objects.create(description=description, amount=amount)
        return redirect('/')

    return render(request, "index.html", context={
        "transactions": Transactions.objects.all(),
        "income": Transactions.objects.filter(amount__gt=0).aggregate(sum=Sum("amount"))["sum"] or 0,
        "expense": Transactions.objects.filter(amount__lt=0).aggregate(sum=Sum("amount"))["sum"] or 0,
        "total_balance": Transactions.objects.aggregate(sum=Sum("amount"))["sum"] or 0
    })


def deleteTransaction(request, uuid):
    Transactions.objects.filter(uuid=uuid).delete()
    return redirect('/')