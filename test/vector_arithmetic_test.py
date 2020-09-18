from unittest import TestCase

from src.app.models import Vector
from src.app.vector_arithmetic import (
    modulate_vector,
    avg_vector,
    angle_from_origin_to_vector,
)


class VectorArithmeticTestCase(TestCase):
    def test_modulate_vector(self):
        origin = Vector(12.4, 43.6)
        vector = Vector(22.5, 23.3)
        modulator = 3.5
        new_vector = modulate_vector(origin, vector, modulator)
        self.assertEqual(new_vector, Vector(35.35, -71.05))

    def test_avg_vector(self):
        vectors = [
            Vector(54.39, 57.68),
            Vector(38.76, 15.40),
            Vector(70.17, 45.42),
        ]
        result = avg_vector(vectors)
        self.assertEqual(result, Vector(54.44, 39.50))

    def test_angle_from_origin_to_vector(self):
        origin = Vector(25.38, 42.69)
        vector = Vector(70.76, 57.41)
        result = angle_from_origin_to_vector(origin, vector)
        self.assertEqual(result, 0.3136637626332259)
