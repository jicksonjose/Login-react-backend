
from django.urls import path, include
from . import views
urlpatterns = [

    path('login/',  include('api.v1.auth.urls')),
    path('register/',  include('api.v1.register.urls'))
   
]
