from django.urls import path

from .views import ActorDetail, ActorList, MovieDetail, MovieList, review_list

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('actor', ActorList.as_view()),
    path('actor/<int:pk>', ActorDetail.as_view()),
    path('movies/<int:pk>/reviews', review_list),
]
