from django.urls import path
from .views import get_user
from .views import update_user

urlpatterns = [
    path('get_user/', get_user),
    path('update_user/', update_user)
]
