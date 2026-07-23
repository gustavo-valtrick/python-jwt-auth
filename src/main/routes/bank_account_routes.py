from flask import Blueprint, jsonify, Response, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.user_register_composer import user_register_composer
from src.main.composer.login_creator_composer import login_creator_composer
from src.main.composer.balance_editor_composer import balance_editor_composer

bank_routes_bp = Blueprint(name="bank_routes", import_name=__name__, url_prefix="/bank")


@bank_routes_bp.route("/registry", methods=["POST"])
def registry_user() -> tuple[Response, int]:
    http_request = HttpRequest(body=request.get_json())
    http_response = user_register_composer().handle(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/login", methods=["POST"])
def create_login() -> tuple[Response, int]:
    http_request = HttpRequest(body=request.get_json())
    http_response = login_creator_composer().handle(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code


@bank_routes_bp.route("/balance/<user_id>", methods=["PATCH"])
def edit_balance(user_id) -> tuple[Response, int]:
    http_request = HttpRequest(body=request.get_json(), params={"user_id": user_id})
    http_response = balance_editor_composer().handle(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code
