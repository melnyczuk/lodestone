from typing import Any, Dict, List, Union

from .api import API
from .models import Location


api = API()




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
