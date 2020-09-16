from flask import Flask, jsonify, request
from typing import Any, Tuple

from .controller import get_rated_places

server = Flask(__name__)


@server.route("/ratings", methods=["GET"])
def _ratings() -> Tuple[str, int]:
    get_rated_places(request.args)
    return ("", 202)  # return id from celery task


@server.route("/ping", methods=["GET"])
def _ping() -> Tuple[Any, int]:
    return (jsonify("pong"), 200)


@server.errorhandler(400)
def _four_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(str(e)), 400)


@server.errorhandler(403)
def _four_oh_three(e: object) -> Tuple[Any, int]:
    return (jsonify(str(e)), 403)


@server.errorhandler(404)
def _four_oh_four(e: object) -> Tuple[Any, int]:
    return (jsonify(str(e)), 404)


@server.errorhandler(500)
def _five_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(str(e)), 500)
