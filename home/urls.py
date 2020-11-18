from django.urls import path
from django.contrib import admin
from parents import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('admin/', admin.site.urls, name="administrator"),
]
