# coding=utf-8
import json
import requests

from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse  # noqa

PATH = "/open_api/v1.2/oauth2/access_token/"
APP_ID = 7049612972288638977
AUTH_CODE = d928aa8468f5ed8715438bca3e3b7cc79b14e0a
SECRET = b1a7817708af948fbbd62a12403246acf908f087


def build_url(path, query=""):
    # type: (str, str) -> str
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))

def post(json_str):
    # type: (str) -> dict
    """
    Send POST request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    url = build_url(PATH)
    args = json.loads(json_str)
    headers = {
        "Content-Type": "application/json",
    }
    rsp = requests.post(url, headers=headers, json=args)
    return rsp.json()

if __name__ == '__main__':
    secret = SECRET
    app_id = APP_ID
    auth_code = AUTH_CODE

    # Args in JSON format
    my_args = "{\"secret\": \"%s\", \"app_id\": \"%s\", \"auth_code\": \"%s\"}" % (secret, app_id, auth_code)
    print(post(my_args))