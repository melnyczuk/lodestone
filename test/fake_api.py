def fake_search_nearby(*args):
    return [
        {
            "place_id": "first_id",
            "location": {
                "lat": 51.55332019999999,
                "lng": -0.0358568,
            },
        },
        {
            "place_id": "second_id",
            "location": {
                "lat": 51.55291319999999,
                "lng": -0.0351565,
            },
        },
        {
            "place_id": "third_id",
            "location": {
                "lat": 51.55274439999999,
                "lng": -0.0359406,
            },
        },
    ]


def fake_get_ratings(*args):
    return [
        {
            "place_id": "first_id",
            "rating": 4.5,
        },
        {
            "place_id": "second_id",
            "rating": 3.2,
        },
        {
            "place_id": "third_id",
            "rating": 2.6,
        },
    ]
