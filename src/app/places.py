from typing import Any, Dict, List, Union

from .api import API
from .geodesy import locations_to_vectors
from .models import Location
from .vector_arithmetic import (
    modulate_vector,
    avg_vector,
    angle_from_origin_to_vector,
)


api = API()


def main(data: Dict[str, Any]):
    current_location = Location(**data)
    nearby_locations, ratings = get_nearby_locations_and_ratings(
        current_location
    )
    (current_vector, *vectors) = locations_to_vectors(
        [current_location, *nearby_locations]
    )
    vector_rating_tuples = zip(vectors, ratings)
    modulated_vectors = [
        modulate_vector(current_vector, vector, rating)
        for (vector, rating) in vector_rating_tuples
    ]
    avg = avg_vector(modulated_vectors)
    ang = angle_from_origin_to_vector(current_vector, avg)
    return ang + 90


def get_nearby_locations_and_ratings(
    location: Location,
) -> Union[List[Location], List[float]]:
    place_ids, locations = zip(
        *[
            (loc["place_id"], Location(**loc["location"]))
            for loc in api.search_nearby(location)
        ]
    )
    ratings: List[float] = [rat["rating"] for rat in api.get_ratings(place_ids)]
    return list(locations), ratings
