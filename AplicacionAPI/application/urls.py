from django.urls import path
from .views import home, peticiones, informacion

urlpatterns = [
    path('', home, name = 'home'),
    path('peticiones/', peticiones, name = 'peticiones'),
    path('informacion/', informacion, name = 'informacion'),
]
