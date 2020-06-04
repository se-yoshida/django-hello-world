from django.urls import path
from . import views

app_name = 'hello_world'

urlpatterns = [
    path('', views.index, name='index'),
]