#!/usr/bin/env python3
""" Session Authorization """
import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ session class """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ method that create a session """
        if user_id and isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        method that return a User ID based on a Session ID
        """
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """ return a User """
        if request:
            session_id = self.session_cookie(request)
            user_id = self.user_id_for_session_id(session_id)

            return User.get(user_id)

    def destroy_session(self, request=None):
        """ method that delete a session """
        if request:
            session_id = self.session_cookie(request)
            if session_id and self.user_id_for_session_id(session_id):
                del self.user_id_by_session_id[session_id]
                return True
        return False
