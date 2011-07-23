"""
github3.models
~~~~~~~~~~~~~~

This module provides the Github3 object model.
"""

from .helpers import to_python, to_api


class BaseResource(object):
    """A BaseResource object."""

    _strs = []
    _ints = []
    _dates = []
    _bools = []
    _map = {}


    def __init__(self):
        self._bootstrap()
        super(BaseResource, self).__init__()


    def __dir__(self):
        d = self.__dict__.copy()

        try:
            del d['_gh']
        except KeyError:
            pass

        return d.keys()


    def _bootstrap(self):
        """Bootstraps the model object based on configured values."""

        for attr in (self._strs + self._ints + self._dates + self._bools + self._map.keys()):
            setattr(self, attr, None)


    @classmethod
    def new_from_dict(cls, d, gh=None):

        return to_python(
            obj=cls(), in_dict=d,
            str_keys = cls._strings,
            int_keys = cls._ints,
            date_keys = cls._datetimes,
            bool_keys = cls._booleans,
            _gh = gh
        )


class User(BaseResource):
    """Github User object model."""

    _strings = ['login', 'gravatar_url', 'url', 'name', 'company',
        'blog', 'location', 'email', 'bio', 'html_url']

    _ints = ['id', 'public_repos', 'public_gists', 'followers', 'following']
    _datetimes = ['created_at',]
    _booleans = ['hireable', ]
    _map = {}


    def __init__(self):
        super(User, self).__init__()

    def __repr__(self):
        return '<user {0}>'.format(self.login)