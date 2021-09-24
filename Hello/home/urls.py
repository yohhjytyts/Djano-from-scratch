from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('employee/planning',views.employe_planning,name='employe'),
    path('employee/viewplanning',views.employe_viewplanning,name='employe'),
    path('login', auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path('logout', views.logout,name='logout'),
]