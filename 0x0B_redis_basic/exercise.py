#!/usr/bin/env python3
"""
Redis basic module
"""
from typing import Union, Callable, Optional
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper

    def call_history(method: callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs
        for a particular function.
        """
        @wraps(method)
        def wrapper(self, *args):
            """
            wrapper function
            """
            self._redis.rpush("{}:inputs".format(method.__qualname__),
                              str(args))
            result = method(self, *args)
            self._redis.rpush("{}:outputs".format(method.__qualname__),
                              str(result))
            return result
        return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ __init __ """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Takes a data argument and returns a string.
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """  Reading from Redis and recovering original type
        """
        value = self._redis.get(key)
        try:
            value = fn(value)
        except Exception:
            pass
        return value
