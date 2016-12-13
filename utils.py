# -*- coding: utf-8 -*-
import requests
from bottle import response

import settings

__author__ = 'mkr'


def get_random_word():
    """ Returns a random word fetched from Wikipedia.
    :return string which is a drawn word from Wikipedia.
    """

    resp = requests.get(url=settings.RANDOM_WORD_PUBLIC_API)

    if resp.status_code == requests.codes.ok:
        return resp.content
    return None


def get_word_meaning(word):
    """ Returns a meaning of provided word including simple definition and article contend from Wikipedia.
    :return tuple of strings where first parameter is a definition, second is a article content
    """

    definition = get_word_definition(word)
    article_content = get_article_content(word)
    return definition, article_content


def get_word_definition(word, limit=1, _format="json"):
    """ Returns a definition of provided word from Wikipedia.
    :return string which represents a word definition
    """

    params = {
        "action": "opensearch",
        "search": word,
        "limit": limit,
        "namespace": 0,
        "format": _format
    }
    resp = requests.get(url=settings.WIKIPEDIA_API, params=params)
    if resp.status_code == requests.codes.ok:
        data = resp.json()

        definition = data[2][0] if data[2] else settings.NOT_FOUND_MESSAGE
        return definition
    return None


def get_article_content(word, _format="json"):
    """ Returns a article content of provided word from Wikipedia.
    :return string which represents an article content
    """

    params = {
        "action": "parse",
        "section": 0,
        "prop": "text",
        "page": word,
        "format": _format
    }
    resp = requests.get(url=settings.WIKIPEDIA_API, params=params)
    if resp.status_code == requests.codes.ok:
        data = resp.json()

        if "parse" in data and "text" in data["parse"]:
            return data["parse"]["text"]
        elif "error" in data and "info" in data["error"]:
            return data["error"]["info"]
        return "No results"
    return None


def get_joke(first_name=None, last_name=None):
    """ Returns a random joke from icndb.com API.
    :param first_name string
    :param last_name string
    :return string which represents a joke content
    """

    params = {}

    if first_name:
        params.update({"firstName": first_name})

    if last_name:
        params.update({"lastName": last_name})

    if not params:
        params = {
            "firstName": "Chuck",
            "lastName": "Norris"
        }

    resp = requests.get(url=settings.JOKES_API, params=params)
    if resp.status_code == requests.codes.ok:
        data = resp.json()
        if data["type"] == "success":
            return data["value"]["joke"]
        return None


def errorhandler(func):
    """ This is a decorator which is responsible of error handling.
    :return wrapped function
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception, e:
            response.status = 400
            return {
                "error": str(e),
                "error_type": e.__class__.__name__
            }

    return wrapper
