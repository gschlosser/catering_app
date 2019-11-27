from flask import Blueprint, request, redirect
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from services.user_service import create_user
from models.users import Users
from services import bcrypt
from . import blacklist, jwt


autho_blueprint = Blueprint('auth_api', __name__)

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

@autho_blueprint.route('/register', methods=['POST'])
def register():
    body = request.json
    
    try: 
        return create_user(body['email'], bcrypt.generate_password_hash(body['password']).decode('utf-8'))
    except Exception as e:
        return str(e), 400
    return {'message': 'successfully created new user'}
    



@autho_blueprint.route('/login', methods=['POST'])
def login():
    body = request.json
    
    check_if_user_exists = Users.query.filter_by(email=body['email']).first()
    if bcrypt.check_password_hash(check_if_user_exists.password, body['password']):
        access_token = create_access_token(check_if_user_exists.id)
        return {
            'message': 'hey logged in!',
            'token': access_token
        }
    else:
        return 'incorrect password try again'
        
    


@autho_blueprint.route('/logout', methods=['POST'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return 'successfully logged out!' 
