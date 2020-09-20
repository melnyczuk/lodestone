from flask import Flask, jsonify, request
from celery.result import AsyncResult  # type: ignore
from typing import Any, Tuple

from .celery import celery
from .logger import logger
from .tasks import ratings

server = Flask(__name__)
celery.conf.update(server.config)

logger.log("lodestone is ready 🧭")


@server.route("/ratings", methods=["POST"])
def post_ratings_geolocation() -> Tuple[str, int]:
    data = request.json

    if "lat" not in data or "lng" not in data:
        logger.request(400)
        return ("missing valid lat & lng data for this request", 400)

    result = ratings.delay(float(data["lat"]), float(data["lng"]))

    logger.request(202)
    return (jsonify(result), 202)


@server.route("/ratings/<id>", methods=["GET"])
def get_ratings_orientation(id: str) -> Tuple[Any, int]:
    task = AsyncResult(id, app=celery)

    if not task.ready():
        logger.request(202)
        return (task.state, 202)

    if task.failed():
        logger.request(500)
        return (jsonify(str(task.result)), 500)

    logger.request()
    return (jsonify(task.get()), 200)


@server.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    logger.request()
    return (jsonify("pong"), 200)


@server.errorhandler(400)
def four_hundred(e: object) -> Tuple[Any, int]:
    logger.request(400)
    return (jsonify(str(e)), 400)


@server.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    logger.request(403)
    return (jsonify(str(e)), 403)


@server.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    logger.request(404)
    return (jsonify(str(e)), 404)


@server.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    logger.request(500)
    return (jsonify(str(e)), 500)
