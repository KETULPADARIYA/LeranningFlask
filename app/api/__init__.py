from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, users, posts, comments, errors



"""
Thursday:
    Started learning Restful Api in Flask
Today:
    I will develop flask API,today. 
Blockers:
    No blockers
"""