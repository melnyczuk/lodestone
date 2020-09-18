from unittest import TestCase, mock, skip

import numpy as np

from src.app.api import API
from src.app.places import main, get_nearby_locations_and_ratings
from src.app.models import Location, Vector

from test.fake_api import fake_search_nearby, fake_get_ratings

data = {"lat": 51.5527444, "lng": -0.0359406}


class PlacesTestCase(TestCase):
    @mock.patch.object(API, "search_nearby", fake_search_nearby)
    @mock.patch.object(API, "get_ratings", fake_get_ratings)
    def test_main(self):
        result = main(data)
        self.assertEqual(result, 91.44799114680296)

    @mock.patch.object(API, "search_nearby", fake_search_nearby)
    @mock.patch.object(API, "get_ratings", fake_get_ratings)
    def test_get_nearby_locations_and_ratings(self):
        locations, ratings = get_nearby_locations_and_ratings(data)
        self.assertEqual(ratings, [4.5, 3.2, 2.6])
        self.assertEqual(
            locations,
            [
                Location(51.55332019999999, -0.0358568),
                Location(51.55291319999999, -0.0351565),
                Location(51.55274439999999, -0.0359406),
            ],
        )
