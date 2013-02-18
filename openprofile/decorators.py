from flask import request
from flask import session
from flask import abort

from werkzeug.contrib.cache import SimpleCache
from functools import wraps

cache = SimpleCache()

def cached(timeout=60*5, key='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator

def authorized():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not 'auth' in session:
                session.pop('auth', None)
                abort(403)
            rv = f(*args, **kwargs)
            return rv
        return decorated_function
    return decorator