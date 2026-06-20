from flask import jsonify, request, abort
from service import app
from service.models import Account, DataValidationError
@app.route("/", methods=["GET"])
def index():
    return jsonify({"name":"Account REST API Service","version":"1.0"}), 200
@app.route("/accounts", methods=["POST"])
def create_accounts():
    account = Account().deserialize(request.get_json())
    account.create()
    return jsonify(account.serialize()), 201
@app.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify([a.serialize() for a in Account.all()]), 200
@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        abort(404)
    return jsonify(account.serialize()), 200
@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        abort(404)
    account.deserialize(request.get_json())
    account.update()
    return jsonify(account.serialize()), 200
@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", 204
