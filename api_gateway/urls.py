from django.urls import path
from .views import all_tutoring
from .views import get_tutoring
from .views import delete_tutoring
from .views import create_tutoring
from .views import update_tutoring

urlpatterns = [
    path('all_tutoring/', all_tutoring),
    path('get_tutoring/', get_tutoring),
    path('delete_tutoring/', delete_tutoring),
    path('create_tutoring/', create_tutoring),
    path('update_tutoring/', update_tutoring)
]
