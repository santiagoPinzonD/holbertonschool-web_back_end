#!/usr/bin/env python3
""" Module of auth
"""
import re
from flask import request
from typing import List, TypeVar


class Auth():
    """ class auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method """
        if path and excluded_paths:
            if path[-1] != '/':
                path += '/'
            for route in excluded_paths:

                path = path.replace('/', '')
                route = route.replace('/', '')

                if route[-1] == '*':
                    route = route.replace('*', '.*')

                if re.search(route, path):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ auth header method """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user method """
        return None
