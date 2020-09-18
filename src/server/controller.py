from typing import Any, Dict, List

from src.app.models import Location
from src.app.places import main as _ratings

from .celery import celery


@celery.task  # type: ignore
def ratings(data: Dict[str, Any]) -> float:
    return _ratings(data)
