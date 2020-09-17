from typing import Any, Dict, List

from src.api import API
from src.celery import celery
from src.models import Location, RatedPlace

api = API()


@celery.task  # type: ignore
def main(data: Dict[Any, Any]) -> List[RatedPlace]:
    location = Location(**data)
    return get_rated_places(location)


def get_rated_places(location: Location) -> List[RatedPlace]:

    locations: Dict[str, Location] = {
        loc["place_id"]: loc["location"] for loc in api.search_nearby(location)
    }

    place_ids = list(locations.keys())

    ratings: Dict[str, float] = {
        rat["place_id"]: rat["rating"] for rat in api.get_ratings(place_ids)
    }

    places = [
        RatedPlace(
            id=place_id, location=locations[place_id], rating=ratings[place_id]
        )
        for place_id in place_ids
        if place_id in ratings.keys()
    ]
    raise Exception("test failure")
    return places
