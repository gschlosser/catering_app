from . import bcrypt

def generate_password(password):
    my_hash = bcrypt.generate_password_hash(password)

    return my_hash