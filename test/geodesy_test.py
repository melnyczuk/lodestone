from unittest import TestCase
import numpy as np

from src.app.models import Location, Vector
from src.app.geodesy import locations_to_vectors


class GeodesyTestCase(TestCase):
    def test_locations_to_vectors(self):
        data = [
            Location(51.55332019999999, -0.0358568),
            Location(51.55291319999999, -0.0351565),
            Location(51.55274439999999, -0.0359406),
        ]
        vectors = [
            Vector(705488.3907780526, 5715523.697589938),
            Vector(705538.7645656705, 5715480.415717953),
            Vector(705485.1786193727, 5715459.444234611),
        ]
        result = locations_to_vectors(data)
        assertions = [np.array_equal(*arrs) for arrs in zip(result, vectors)]
        self.assertNotIn(False, assertions)
