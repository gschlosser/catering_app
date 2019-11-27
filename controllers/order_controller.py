from flask_jwt import jwt_required
from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.order_service import create_order, fetch_order



order_controller = Blueprint('catering_api', __name__)

@order_controller.route('/new', methods = ['POST'])
@jwt_required
def new_order():
    user = get_jwt_identity()
    data = request.json

    return create_order(
        data,
        user
    )

@order_controller.route('/get_orders', methods = ['GET'])
@jwt_required
def get_orders_by_id():
    user = get_jwt_identity()
    orders = fetch_order(user)
    return custom_response(orders, 200)

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )

