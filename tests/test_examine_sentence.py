import pytest
from hamcrest import assert_that, close_to, is_

from examine_sentence import *

SENTENCES = [
    (
        "Of course... we know that we can write a Python program,"
        " and, more importantly, use this as the start of both"
        " an English and Computer Science combo lesson!"
    ),
    "Hello, my name is Tom.",
    "your work will focus on three functions.",
    "you will need to make use of Python's built-in str complete functions to...",
    'I told my friend Adam the following, "the Loch Ness Monster wants "tree fitty."',
]


@pytest.mark.parametrize(
    "sentence, found_or_not", zip(SENTENCES, [True, True, False, False, True])
)
def test_first_letter_is_capitalized(sentence: str, found_or_not: bool):
    assert_that(first_letter_is_capitalized(sentence), is_(found_or_not))


@pytest.mark.parametrize(
    "sentence, found_or_not", zip(SENTENCES, [True, True, True, True, False])
)
def test_ends_with_punctuation(sentence: str, found_or_not: bool):
    assert_that(ends_with_punctuation(sentence), is_(found_or_not))


@pytest.mark.parametrize(
    "sentence, found_or_not", zip(SENTENCES, [True, True, False, True, True])
)
def test_includes_advanced_punctuation(sentence: str, found_or_not: bool):
    assert_that(includes_advanced_punctuation(sentence), is_(found_or_not))
