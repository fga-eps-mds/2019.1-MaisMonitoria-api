from .views import all_tutoring, get_tutoring, create_tutoring, delete_like, delete_tutoring
from .views import update_tutoring, search_tutoring, like_tutoring
from django.urls import path

urlpatterns = [
    path('all_tutoring/', all_tutoring),
    path('get_tutoring/', get_tutoring),
    path('create_tutoring/', create_tutoring),
    path('update_tutoring/', update_tutoring),
    path('search_tutoring/', search_tutoring),
    path('delete_tutoring/', delete_tutoring),
    path('like_tutoring/', like_tutoring),
    path('like_delete/', delete_like),
]
