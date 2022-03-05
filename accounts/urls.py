from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('overview/', views.overview),
    path('search/', views.search,name="search-any"),
    #path('filter/', views.filter,name="filter-any"),
    path('dashboard/',views.home),

    ]

