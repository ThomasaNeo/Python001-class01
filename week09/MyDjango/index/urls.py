from django.urls import path, re_path, register_converter
from . import views, converters


urlpatterns = [
    path('', views.index),
    path('login2', views.login2)

]
