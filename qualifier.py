"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re
import collections
import itertools

AnyType = typing.TypeVar("AnyType")


class Article:
    """The `Article` class you need to write for the qualifier."""

    article_id = itertools.count()

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.id = next(self.article_id)
        self.last_edited = None

    def __repr__(self):
        return "<Article title=" + repr(self.title) + " author=" + repr(self.author) + " publication_date=" + \
               repr(datetime.datetime.isoformat(self.publication_date)) + ">"

    def __len__(self):
        return len(self.content)

    def short_introduction(self, n_characters: int):
        if len(self.content) <= n_characters:
            return self.content

        intro = self.content[0:n_characters + 1]
        last_space = intro.rfind(" ")
        last_newline = intro.rfind("\n")
        highest_index = max(last_newline, last_space)
        return self.content[:highest_index]

    def most_common_words(self, n_words: int):
        lowercase = self.content.lower()
        regexed = re.sub('[^0-9a-zA-Z]', " ", lowercase)
        words = regexed.split()
        word_count = collections.Counter(words)
        most_freq = dict(word_count.most_common(n_words))

        return most_freq

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, new_content: str) -> None:
        self._content = new_content
        self.last_edited = datetime.datetime.now()

    def __lt__(self, other_article):

        if not isinstance(other_article, Article):
            return NotImplemented

        return self.publication_date < other_article.publication_date


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
