import os
import requests
from dataclasses import dataclass

from typing import List, TypedDict
from requests import Response

ROD_URL = os.getenv("ROD_URL", "localhost:9891")
URL = f"{ROD_URL}/google/places"


@dataclass(frozen=True)
class Place(TypedDict):
    lat: float
    lng: float


@dataclass(frozen=True)
class API:
    def fetch_place_data(self: "API", place: Place) -> List:
        response: Response = requests.get(URL, vars(place))
        return response.json().get('results', [])
