from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies.models import Actor, Movie, Review

from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def movie_list(request):
  if request.method == 'GET':
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=200)
  elif request.method == 'POST':
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def movie_detail(request, pk):
  movie = get_object_or_404(Movie, pk=pk)
  if request.method == 'GET':
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=200)
  elif request.method == 'PATCH':
    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)
  elif request.method == 'DELETE':
    movie.delete()
    return Response(status=204)

@api_view(['GET', 'POST'])
def actor_list(request):
  if request.method == 'GET':
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data, status=200)
  elif request.method == 'POST':
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def actor_detail(request, pk):
  actor = get_object_or_404(Actor, pk=pk)
  if request.method == 'GET':
    serializer = ActorSerializer(actor)
    return Response(serializer.data, status=200)
  elif request.method == 'PATCH':
    serializer = ActorSerializer(actor, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=200)
    return Response(serializer.errors, status=400)
  elif request.method == 'DELETE':
    actor.delete()
    return Response(status=204)
  
@api_view(['GET', 'POST'])
def review_list(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=401)