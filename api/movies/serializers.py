from rest_framework import serializers
from .models import Movie, MovieStatus

from datetime import date


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
