from ninja import Router
from .models import Movie
from .serializers import MovieSerializer
from ms_cinema.scheduler import scheduler


movies_api = Router()


# Create your views here.
@movies_api.post("")
def create_movie(request):
    post_data = request.POST.copy()
    post_data["poster"] = request.FILES["poster"]
    serializer = MovieSerializer(data=post_data)
    if serializer.is_valid():
        Movie(serializer).save(using="sync_mongo")
        return 200, serializer.data
    return 400, serializer.errors


@movies_api.get("")
def get_all_movies(_request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return 200, list(serializer.data)


@movies_api.get("trending")
def get_all_movies_by_ranking(_request):
    movies = reversed(Movie.objects.using("sync_mongo").order_by("ranking").all())
    serializer = MovieSerializer(movies, many=True)
    return 200, serializer.data
