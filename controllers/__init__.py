from flask_jwt_extended import JWTManager

jwt = JWTManager()
blacklist = set()



from .autho_controller import autho_blueprint
from .order_controller import order_controller
