from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Location:
    lat: float
    lng: float


@dataclass(frozen=True)
class RatedPlace:
    id: str
    location: Location
    rating: float


@dataclass(frozen=True)
class Vector:
    x: float
    y: float

    def toList(self: "Vector") -> List[float]:
        return [self.x, self.y]
