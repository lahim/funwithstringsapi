# -*- coding: utf-8 -*-
from collections import Counter
import utils

__author__ = 'mkr'


class User(object):
    """ This class represents a simple user model.
    """

    def __init__(self, username):
        self.username = username
        self.token = None

    @classmethod
    def create(cls, username, token=None):
        """ Creates and returns a created user based on provided username and token. If token was not provided,
        then it is going to be generated automatically.
        """

        user = cls(username=username)
        if token is None:
            user.token = utils.generate_token()
        else:
            user.token = token
        return user

    @classmethod
    def find_user_by_token(cls, token):
        """ This is a simple method which is responsible for searching users based on provided token in mock list of users.
        If user exists, then returns a User object, else None.
        :param token string
        :return User object or None
        """

        from mock import Mock
        users = filter(lambda u: u.token == token, Mock.users)
        return users[0] if len(users) == 1 else None


class Result(object):
    """ This class represents a response result object which is able to serve data in JSON or XML format.
    XML format is not supported yet.
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def to_json(self):
        """ Returns a dict of provided arguments for result object.
        :return dict
        """

        return self.kwargs

    def to_xml(self):
        """ Returns a xml content of provided arguments for result object.
        This method is not implemented yet.
        :return string
        """

        # todo: implement this method
        raise NotImplementedError("Method to_xml is not implemented")


class Word(object):
    """ This class represents a simple word fetched from Wikipedia, including its meaning (definition, article content).
    """

    counter = Counter()  # holds all statistic

    def __init__(self, text, definition=None, article_content=None):
        self.text = text
        self._definition = definition
        self._article_content = article_content
        self.counter[text] += 1

    @property
    def definition(self):
        """ Returns a simple definition of selected word fetched from OpenSearch Wikipedia API.
        :return string
        """

        if self._definition is None:
            self._load_data()
        return self._definition

    @property
    def article_content(self):
        """ Returns an article content of selected word fetch from Wikipedia API.
        :return string
        """

        if self._article_content is None:
            self._load_data()
        return self._article_content

    @classmethod
    def get_random_word(cls):
        """ Returns a random word fetched from Wikipedia.
        :return string
        """

        random_word_text = utils.get_random_word()
        word = cls(text=random_word_text)
        word._load_data()
        return word

    @classmethod
    def get_statistic(cls, limit):
        """ Returns statistics for most popular words fetched from Wikipedia.
        :return Result object
        """

        return Result(statistic=dict(cls.counter.most_common(limit)))

    def to_json(self):
        """ Returns a JSON content which is a representation of selected word using Result object.
        :return dict
        """

        return Result(word=self.text, definition=self.definition, article_content=self.article_content).to_json()

    def to_xml(self):
        """ Returns a XML content which is a representation of selecte dword using Result object.
        :return string
        """

        return Result(word=self.text, definition=self.definition, article_content=self.article_content).to_xml()

    def _load_data(self):
        """ This method loads a definition and article content of provided word from Wikipedia.
        """

        self._definition, self._article_content = utils.get_word_meaning(word=self.text)


class Joke(object):
    """ This class represents a simple joke fetched from icndb.com.
    """

    @classmethod
    def get_random_joke(cls, first_name=None, last_name=None):
        """ Returns a random joke fetched from remote API.
        :return Result object
        """

        return Result(text=utils.get_joke(first_name=first_name, last_name=last_name))
