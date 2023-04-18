from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from datetime import date


class MovieStatus(models.TextChoices):
    COMINGUP = "CU", _("Coming Up")
    STARTING = "ST", _("Starting")
    RUNNING = "RU", _("Running")
    FINISHED = "FN", _("Finished")


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=255, blank=False)
    protagonists = models.CharField(max_length=255, default='')
    poster = models.ImageField(upload_to='upload/movies/posters/')
    start_date = models.DateField(default=date.today)
    status = models.CharField(max_length=2, choices=MovieStatus.choices, default=MovieStatus.COMINGUP)
    ranking = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['ranking'])
        ]

    def __str__(self) -> str:
        return self.name


@receiver(signals.post_save, sender=Movie)
def movie_post_save_receiver(instance: Movie, using, **kwargs):
    if using == "sync_mongo":
        return
    instance.save(using="sync_mongo")


@receiver(signals.post_delete, sender=Movie)
def move_post_delete_receiver(instance: Movie, using, **kwargs):
    if using == "sync_mongo":
        return
    instance.delete(using="sync_mongo")
