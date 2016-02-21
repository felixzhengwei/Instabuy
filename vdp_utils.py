import requests
from calendar import timegm
from datetime import datetime
from hashlib import sha256
from urlparse import urlparse
import hmac
"""
vdp_utils
~~~~~~~~~
This module provides various helpers for calling vdp apis
"""


def _get_x_pay_token(shared_secret, resource_path, query_string, body):
    if not body:
        body = ''
    timestamp = str(timegm(datetime.utcnow().timetuple()))
    pre_hash_string = timestamp + resource_path + query_string + body
    hash_string = hmac.new(shared_secret,
                           msg=pre_hash_string,
                           digestmod=sha256).hexdigest()
    return 'xv2:' + timestamp + ':' + hash_string


def _get_resource_path(path):
    pos = path.find('/')
    base = path[:pos]
    if base == 'vts':
        return path
    return path[pos+1:]


class XToken(requests.auth.AuthBase):
    """X pay token authentication hook"""

    def __init__(self, shared_secret):
        self.shared_secret = shared_secret

    def __call__(self, r):
        url = urlparse(r.url)
        resource_path = _get_resource_path(url.path[1:])
        query_string = '&'.join(sorted(url.query.split('&')))
        body = r.body
        token = _get_x_pay_token(self.shared_secret, resource_path,
                                query_string, body)
        r.headers['x-pay-token'] = token
        return r


class XSession(requests.Session):
    """Requests Session for xpaytoken apis
    Construct as XSession(apikey, shared_secret), usage same as
    requests.Session
    """

    def __init__(self, apikey, shared_secret):
        super(XSession, self).__init__()
        self.params['apikey'] = apikey
        self.auth = XToken(shared_secret)


class MSession(requests.Session):
    """Requests Session for mutualauth(2-way SSL) apis
    username, password: App credentials
    cert: path to app's client certificate
    key: path to app's private key
    """

    def __init__(self, username, password, cert, key):
        super(MSession, self).__init__()
        self.cert = (cert, key)
        self.auth = (username, password)