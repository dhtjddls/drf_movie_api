from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Actor, Movie, Review

from .serializers import ActorSerializer, MovieSerializer, ReviewSerializer


class MovieList(APIView):
  def get(self, request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=200)
    
  def post(self, request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class MovieDetail(APIView):
    def get_object(self, pk):
        movie = get_object_or_404(Movie, pk=pk)
        return movie

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def patch(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=204)

  
class ActorList(APIView):
  def get(self, request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many=True)
    return Response(serializer.data, status=200)
  
  def post(self, request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


class ActorDetail(APIView):
    def get_object(self, pk):
        actor = get_object_or_404(Actor, pk=pk)
        return actor

    def get(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def patch(self, request, pk):
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        actor = self.get_object(pk)
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