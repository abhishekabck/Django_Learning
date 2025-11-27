from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import StudentForm
from .models import *
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

# Create your views here.
def index(request):
    context = {'form': StudentForm}
    if request.method == "POST":
        name = request.POST.get("full_name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        upload_file = request.FILES.get("upload_file")
        Student2.objects.create(
            name=name,
            age=age,
            gender=gender,
            upload_file=upload_file,
        )
        return redirect("/thank-you")
    return render(request, "index.html", context)
def contact(request):
    return HttpResponse("Thank you Contact us!!")

def dynamic_route(request, number):
    for i in range(1, 11):
        print(76,'x', i, '=', i*number)
    return HttpResponse(f"Response by dynamic route<br>You entered {number}")

def table(request, number):
    response = "<table border='1'>"
    for i in range(1, 11):
        response += f"<tr><td>{number}</td><td>x</td><td>{i}</td> <td>= </td> <td>{i*number}</td></tr>"
    response += "</table>"
    return HttpResponse(response)

def dynamic_route_error(request, string):
    return HttpResponse(f"Only Number entry is Allowed!")

def vote_eligibility(request, age):
    context = {
        "age": age,
    }
    return render(request, "voting.html", context)

def Thankyou(request):
    return HttpResponse("Thank you! your Response is recorded.")

def search_page(request):
    students = Student.objects.all()
    search = request.GET.get("search", "")
    age_range = request.GET.get("age_range")
    if search:
        students = students.filter(
            Q(name__icontains=search) |
            Q(mobile_number__startswith=search) |
            Q(email__startswith = search) |
            Q(email__endswith = search) |
            Q(gender__startswith=search) |
            Q(student_bio__icontains=search)
        )
    if age_range:
        if age_range == "1":
            students = students.filter(age__gte = 18, age__lt = 20).order_by('age')
        if age_range == "2":
            students = students.filter(age__gte = 20, age__lt = 22).order_by('age')
        if age_range == "3":
            students = students.filter(age__gte = 22, age__lte = 25).order_by('age')
    context = {'students': students, 'search': search}
    return render(request, "search.html", context)

def product(request):
    search = request.GET.get("search", "")
    print(search)
    context = {
        "products": Product.objects.all(),
        'search': search,
    }
    if search:
        # context['products'] = Product.objects.filter(description__search=search) # using full text search
        # search vector 
        context["products"] = Product.objects.annotate(
            search = SearchVector('title', 'category', 'description')
        ).filter(search=search)

    return render(request, "product.html", context)