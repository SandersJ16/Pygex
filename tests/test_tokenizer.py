#!/usr/bin/env python

import pytest
from .. import pygex

@pytest.fixture(params=["+", "*", "?"])
def regex_repetition_token(request):
    return request.param

def test_tokenizer_empty_string():
    assert pygex.tokenize("") == []

def test_tokenizer_no_special_characters():
    assert pygex.tokenize("abc") == ["a", "b", "c"]

def test_tokenizer_character_with_single_repetition_token(regex_repetition_token):
    assert pygex.tokenize("a" + regex_repetition_token) == ["a" + regex_repetition_token]

def test_tokenizer_throws_error_on_only_repetition_token(regex_repetition_token):
    with pytest.raises(pygex.InvalidRegexPattern):
        pygex.tokenize(regex_repetition_token)
