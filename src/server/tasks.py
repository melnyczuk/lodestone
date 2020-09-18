from src.app.places import main as _ratings

from .celery import celery


@celery.task  # type: ignore
def ratings(lat: float, lng: float) -> float:
    return _ratings(lat, lng)
