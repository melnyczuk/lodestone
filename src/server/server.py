import os
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS  # type: ignore
from celery.result import AsyncResult  # type: ignore
from typing import Any, Tuple, Union

from .celery import celery
from .logger import logger
from .tasks import ratings

server = Flask(__name__)
celery.conf.update(server.config)

origins = str(os.getenv("ORIGINS", "")).split(",")
CORS(server, origins=origins)

logger.log("lodestone is ready 🧭")


def make_response(
    result: Union[Any, None] = None,
    error: Union[str, None] = None,
    status: int = 200,
) -> Tuple[str, int]:
    logger.request(status)
    if result:
        return (jsonify({"result": result}), status)
    if error:
        return (jsonify({"error": error}), status)
    else:
        return (jsonify(), 204)


@server.route("/ratings", methods=["POST"])
def post_ratings_geolocation() -> Tuple[str, int]:
    data = request.json

    if "lat" not in data or "lng" not in data:
        return make_response(
            error="missing valid lat & lng data for this request",
            status=400,
        )

    result = ratings.delay(float(data["lat"]), float(data["lng"]))

    return make_response(result=result.id, status=202)


@server.route("/ratings/<id>", methods=["GET"])
def get_ratings_orientation(id: str) -> Tuple[str, int]:
    task = AsyncResult(id, app=celery)

    if not task.ready():
        return make_response(error=task.state, status=202)

    if task.failed():
        return make_response(error=task.state, status=500)

    return make_response(result=task.result)


@server.route("/ping", methods=["GET"])
def ping() -> Tuple[str, int]:
    return make_response(result="pong")


@server.errorhandler(400)
def four_hundred(e: object) -> Tuple[str, int]:
    return make_response(error=str(e), status=400)


@server.errorhandler(403)
def four_oh_three(e: object) -> Tuple[str, int]:
    return make_response(error=str(e), status=403)


@server.errorhandler(404)
def four_oh_four(e: object) -> Tuple[str, int]:
    return make_response(error=str(e), status=404)


@server.errorhandler(500)
def five_hundred(e: object) -> Tuple[str, int]:
    return make_response(error=str(e), status=500)
