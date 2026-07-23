from flask import Blueprint, jsonify, Response

bank_routes_bp = Blueprint(name="bank_routes", import_name=__name__)


@bank_routes_bp.route("/", methods=["GET"])
def hello() -> tuple[Response, int]:
    return jsonify({"hello": "world"}), 200
