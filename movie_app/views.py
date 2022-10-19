from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


@api_view(['GET'])
def director_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def director_detail_view(request, id):
    director = Director.objects.get(id=id)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)