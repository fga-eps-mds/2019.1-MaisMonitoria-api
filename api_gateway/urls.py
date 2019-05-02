from .views import all_tutoring, get_tutoring, create_tutoring, update_tutoring
from django.urls import path

urlpatterns = [
    path('all_tutoring/', all_tutoring),
    path('get_tutoring/', get_tutoring),
    path('create_tutoring/', create_tutoring),
    path('update_tutoring/', update_tutoring)
]
