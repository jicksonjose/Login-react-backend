
from django.urls import path, include
from . import views
urlpatterns = [

    path('api/v1/register',  views.register),
]