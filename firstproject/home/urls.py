from django.urls import path
from .views import index, contact, dynamic_route, table, dynamic_route_error, vote_eligibility, Thankyou, search_page

urlpatterns = [
    path('', index),
    path('contact/', contact),
    path('dynamic_route/<int:number>', dynamic_route),
    path('dynamic_route/<string>', dynamic_route_error),
    path('table/<int:number>', table),
    path('table/<string>', dynamic_route_error),
    path('voting/<int:age>', vote_eligibility),
    path('thank-you', Thankyou),
    path('search-page', search_page),
]