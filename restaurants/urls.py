from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('resturants_in_map/',views.ResturantsInMap.as_view(), name='resturantsinmap'),
]