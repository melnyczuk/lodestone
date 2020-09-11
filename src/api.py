import os
import requests
from requests import Response
from dataclasses import dataclass
from typing import Any, List

from .models import Location


ROD_URL = os.getenv("ROD_URL", "http://0.0.0.0:8080")
URL = f"{ROD_URL}/google/places"


@dataclass
class API:
    def search_nearby(self: "API", location: Location) -> List[Any]:
        response: Response = requests.get(f"{URL}/nearby", vars(location))
        results: List[Any] = response.json() if response.ok else []
        return results

    def get_ratings(self: "API", place_ids: List[str]) -> List[Any]:
        params = {"place_ids": place_ids}
        response: Response = requests.get(f"{URL}/rating", params=params)
        results: List[Any] = response.json() if response.ok else []
        return results
