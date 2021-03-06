from dataclasses import dataclass


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
