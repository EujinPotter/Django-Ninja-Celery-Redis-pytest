from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class MovieListAPIView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # noinspection PyMethodMayBeStatic
    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for created_data in Movie.objects.filter(id=serializer.data["id"]):
                created_data.save(using="sync_mongo")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieTrendingListAPIView(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        movies = reversed(Movie.objects.using("sync_mongo").order_by("ranking").all())
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
