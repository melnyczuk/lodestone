from unittest import TestCase, mock, skip

from src.app.api import API
from src.app.places import main, _get_rated_places, _get_ratings
from src.app.models import Location, RatedPlace

from test.fake_api import fake_search_nearby, fake_get_ratings

data = {"lat": "51.5527444", "lng": "-0.0359406"}


class PlacesTestCase(TestCase):
    @mock.patch.object(API, "search_nearby", fake_search_nearby)
    @mock.patch.object(API, "get_ratings", fake_get_ratings)
    def test_main(self):
        result = main(float(data["lat"]), float(data["lng"]))
        self.assertEqual(result, 91.44799114680296)

    @mock.patch.object(API, "search_nearby", fake_search_nearby)
    @mock.patch.object(API, "get_ratings", fake_get_ratings)
    def test__get_rated_places(self):
        current_location = Location(float(data["lat"]), float(data["lng"]))
        rated_places = _get_rated_places(current_location)
        self.assertEqual(
            rated_places,
            [
                RatedPlace(
                    "first_id", Location(51.55332019999999, -0.0358568), 4.5
                ),
                RatedPlace(
                    "second_id", Location(51.55291319999999, -0.0351565), 3.2
                ),
                RatedPlace(
                    "third_id", Location(51.55274439999999, -0.0359406), 2.6
                ),
            ],
            "should return List[RatedPlace] matching fake api response, filtering out missing keys",
        )

    @mock.patch.object(API, "get_ratings", fake_get_ratings)
    def test__get_ratings(self):
        place_ids = ["first_id", "second_id", "third_id", "fourth_id"]
        ratings = _get_ratings(place_ids)
        self.assertEqual(
            ratings, {"first_id": 4.5, "second_id": 3.2, "third_id": 2.6}
        )
