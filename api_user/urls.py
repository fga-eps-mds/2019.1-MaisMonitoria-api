from .views import get_user, update_user, create_user, get_monitor
from django.urls import path

urlpatterns = [
    path('get_user/', get_user),
    path('update_user/', update_user),
    path('get_monitor/', get_monitor),
    path('create_user/', create_user)
]
