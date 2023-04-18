from rest_framework import serializers
from django.db.models import signals
from django.dispatch import receiver
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


@receiver(signals.post_save, sender=Movie)
def movie_post_save_receiver(instance: Movie, using, created, **kwargs):
    if using == "sync_mongo":
        return
    for record in Movie.objects.filter(id=MovieSerializer(instance).data["id"]):
        record.save(using="sync_mongo")


@receiver(signals.post_delete, sender=Movie)
def move_post_delete_receiver(instance: Movie, using, **kwargs):
    if using == "sync_mongo":
        return
    instance.delete(using="sync_mongo")
