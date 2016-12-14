# -*- coding: utf-8 -*-
from bottle import request, response

from models import User

__author__ = 'mkr'


def auth(token):
    """ Simple auth method which ties to find a user based on provided token in mock users.
    :param token string
    :return User object or None if not exist
    """

    return User.find_user_by_token(token) is not None


def login_required(func):
    """ This is a decorator which is responsible of checking user's authorization token in headers.
    :return wrapped function
    """

    def wrapper(*args, **kwargs):
        auth_token = request.get_header("Authorization")

        if auth(auth_token):
            return func(*args, **kwargs)

        response.status = 401
        return {
            "error": "No credentials provided",
            "error_type": "AuthError"
        }

    return wrapper
