from django.urls import path
from parents import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
]
