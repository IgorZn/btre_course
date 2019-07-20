from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search/', views.search, name='search'),
]


"""
 <int:listing_id> -- это -- http://127.0.0.1:8000/listings/5
            ^                                              ^
            |______________________________________________|
"""