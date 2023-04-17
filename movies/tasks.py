from celery import shared_task


@shared_task()
def update_movie_ranking():
    print("here")
