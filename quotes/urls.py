from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^quotes/$', views.quotes, name='quotes'),
    re_path(r'^quotes/add/$', views.add_quotes, name='add_quotes'),
]
