from models.users import Users

def create_user(email, password):
    #1 check if email exists in db
    #2 hash the password
    #3 create the user
    new_user = Users(email, password)

    #4 save to the database
    return new_user.save()
