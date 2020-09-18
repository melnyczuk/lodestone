from typing import Dict

from src.app.places import main as _ratings

from .celery import celery


@celery.task  # type: ignore
def ratings(data: Dict[str, float]) -> float:
    return _ratings(**data)
