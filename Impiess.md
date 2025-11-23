### Django:-
> - A web framework in python used for developing websites
> - It is useful because it allows `rapid-development`, `admin-pannel`, `middlewares` etc.
> - This is a `battery Included` framework
> - This framework is scalable.
> - It works on micro-level services.

### Requirements:
> - OOPS Concepts (must)
> - Basic Python
> - Monkey Patching
> - decorators
> - Python (intermediate)
> - Basic HTML
> - CSS
> - JAVA SCRIPT
> - SQL
> - ORM (used behind in Django)

### Battery Included
> Availability of required things like admin-panel, middlewares and all.


## Setting Up Django
> - Install Python
> - Create virtual environment: `virtual env`
> - Install Django through pip: `pip install django`
> - 


## Aggregation and Annotation in Django
> - Example models `Author`, and `Book`
> - Count: `book_count = Book.objects.count()`
> - #### To Find Avg
> - > - Library: `from django.db.models import Avg`
> - > - Code: `avg_price = Book.objects.aggregate(avg_price = Avg('price'))`
> - #### TO find Sum
> - > - Library: `from django.db.models import Sum`
> - > - Code: `total_price = Book.objects.aggregate(price = Sum('price'))`
> - #### To find min and max:
> - > All other aggregate functions work the same as above
> - > Library: `from django.db.models import Avg, Sum, Min, Max, Count`
  
## Annotation
> - python replacement of group by
> - syntax: `author = Author.objects.annotate(total_books = Count('book'))`