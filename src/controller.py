from typing import Any, Dict, List

from .api import API
from .models import Location, RatedPlace

api = API()


def get_rated_places(data: Dict[Any, Any]) -> List[RatedPlace]:
    locations = {
        loc["place_id"]: loc["location"]
        for loc in api.search_nearby(Location(**data))
    }
    place_ids = list(locations.keys())
    ratings: Dict[str, float] = {
        rat["place_id"]: rat["rating"] for rat in api.get_ratings(place_ids)
    }
    return [
        RatedPlace(
            id=place_id, location=locations[place_id], rating=ratings[place_id]
        )
        for place_id in place_ids
        if place_id in ratings.keys()
    ]
