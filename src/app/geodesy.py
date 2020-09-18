import utm  # type: ignore
import numpy as np  # type: ignore
from typing import List

from .models import Location, Vector


def locations_to_vectors(locations: List[Location]) -> List[Vector]:
    lats = np.array([loc.lat for loc in locations])
    lngs = np.array([loc.lng for loc in locations])
    utm_mappings = utm.from_latlon(lats, lngs)
    return [Vector(*coords) for coords in zip(*utm_mappings[:2])]
