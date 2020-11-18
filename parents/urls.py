from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('parentsignup', views.parent_signup_view, name="parentsignup"),
    path('parentlogin', LoginView.as_view(template_name='parents/parentlogin.html'), name="parentlogin"),
    path('', views.parentclick_view, name="parentclick"),
    path('parent-dashboard', views.parent_dashboard_view,name="parent-dashboard"),
    path('parent-add-child', views.addchild, name="addchild"),
    path('parent-view-child', views.view_child, name="view_child"),
]
