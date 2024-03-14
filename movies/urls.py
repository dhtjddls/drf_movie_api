from django.urls import path

from .views import (actor_detail, actor_list, movie_detail, movie_list,
                    review_list)

urlpatterns = [
    path('movies', movie_list),
    path('movies/<int:pk>', movie_detail),
    path('actor', actor_list),
    path('actor/<int:pk>', actor_detail),
    path('movies/<int:pk>/reviews', review_list),
]
