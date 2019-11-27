from models.orders import Orders, OrderSchema

from datetime import datetime

order_schema = OrderSchema()

def create_order(data, user):
    new_order = Orders(
        name=data['name'],
        order=data['order'],
        address=data['address'],
        user_id=user,
        date=datetime.utcnow(),
        last_modified=datetime.utcnow()
    )
    try:
        new_order.save()
        message = 'Order saved.'
        return message, 200
    except Exception as e:
        return str(e), 400

def fetch_order(id):
    x = Orders.get_all_orders(id)
    orders_posted = order_schema.dump(x, many=True)
    return orders_posted