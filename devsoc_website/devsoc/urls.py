from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('noticeboard', views.noticeboard, name='noticeboard'),
    path('forum', views.forum, name='forum'),
    path('login', views.login, name='login'),
    path('resources', views.resources, name='resources'),
    path('contact', views.contact, name='contact'),
]