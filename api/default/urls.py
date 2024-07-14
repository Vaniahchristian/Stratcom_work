from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='homeView'),
    path('people', views.peopleView, name='peopleView'),
    path('people/<int:id>', views.peopleDetailsView, name='peopleDetailsView'),
]