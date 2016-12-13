#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, request
from models import Word, Joke
from utils import errorhandler

__author__ = 'mkr'


@route("/")
@errorhandler
def index():
    return "Fun with Strings API!"


@route("/random_word")
@errorhandler
def random_word():
    """ This method serves a meaning of random word from Wikipedia in JSON format. """

    word = Word.get_random_word()
    return word.to_json()


@route("/statistic/<limit:int>")
@errorhandler
def statistics(limit):
    """ This method serves a statistic of most popular randomly selected words."""

    statistic = Word.get_statistic(limit).to_json()
    return statistic


@route("/joke")
@errorhandler
def joke():
    """ This method serves a random joke. """

    first_name = request.params.get("first_name")
    last_name = request.params.get("last_name")
    return Joke.get_random_joke(first_name, last_name).to_json()


def start():
    """ This method starts a bottle server. """

    run(host='localhost', port=8080, debug=True)


if __name__ == "__main__":
    start()
