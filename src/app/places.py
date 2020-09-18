from typing import Dict, List

from .api import API
from .geodesy import locations_to_vectors
from .models import Location, RatedPlace
from .vector_arithmetic import (
    modulate_vector,
    avg_vector,
    angle_from_origin_to_vector,
)


api = API()


def main(lat: float, lng: float) -> float:
    location = Location(lat, lng)

    rated_places = _get_rated_places(location)

    locations = (rp.location for rp in rated_places)
    (origin, *vectors) = locations_to_vectors([location, *locations])

    ratings = (rp.rating for rp in rated_places)
    vector_rating_tuples = zip(vectors, ratings)

    modulated_vectors = [
        modulate_vector(origin, vector, rating)
        for (vector, rating) in vector_rating_tuples
    ]

    avg = avg_vector(modulated_vectors)
    ang = angle_from_origin_to_vector(origin, avg)
    return ang + 90.0


def _get_rated_places(location: Location) -> List[RatedPlace]:
    locations: Dict[str, Location] = {
        loc["place_id"]: Location(**loc["location"])
        for loc in api.search_nearby(location)
    }

    place_ids = list(locations.keys())
    ratings = _get_ratings(place_ids)

    return [
        RatedPlace(
            id=place_id,
            location=locations[place_id],
            rating=ratings[place_id],
        )
        for place_id in place_ids
        if place_id in ratings.keys()
    ]


def _get_ratings(place_ids: List[str]) -> Dict[str, float]:
    return {
        rat["place_id"]: rat["rating"] for rat in api.get_ratings(place_ids)
    }
