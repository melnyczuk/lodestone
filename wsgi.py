from flask import Flask, jsonify

from typing import Any, Tuple

server = Flask(__name__)


@server.route("/ping", methods=["GET"])
def ping() -> Tuple[Any, int]:
    return (jsonify("pong"), 200)


@server.errorhandler(400)
def four_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 400)


@server.errorhandler(403)
def four_oh_three(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 403)


@server.errorhandler(404)
def four_oh_four(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 404)


@server.errorhandler(500)
def five_hundred(e: object) -> Tuple[Any, int]:
    return (jsonify(error=str(e)), 500)
