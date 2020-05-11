from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.verify_password()
def verfiy_password(email,password):
    if not email:
        return  False
    user = User.q