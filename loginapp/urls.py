
from django.urls import path, include
from . import views
urlpatterns = [

    path('login/', views.loginApi),
    path('register/', views.register)
   
]
