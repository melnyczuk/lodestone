from math import atan
from typing import List

from .models import Vector


def modulate_vector(origin: Vector, vector: Vector, modulator: float) -> Vector:
    return Vector(
        (vector.x - origin.x) * modulator,
        (vector.y - origin.y) * modulator,
    )


def avg_vector(vectors: List[Vector]) -> Vector:
    return Vector(
        sum(v.x for v in vectors) / len(vectors),
        sum(v.y for v in vectors) / len(vectors),
    )


def angle_from_origin_to_vector(origin: Vector, vector: Vector) -> float:
    normalised = Vector(vector.x - origin.x, vector.y - origin.y)
    tan_x = normalised.y / normalised.x
    return atan(tan_x)
