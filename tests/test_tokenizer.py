#!/usr/bin/env python

import pytest
from .. import pygex

def regex_repetition_tokens():
    return ["+", "*", "?"]

def test_tokenizer_empty_string():
    assert pygex.tokenize("") == []

def test_tokenizer_no_special_characters():
    assert pygex.tokenize("abc") == ["a", "b", "c"]

@pytest.mark.parametrize("repetition_token", regex_repetition_tokens())
def test_tokenizer_character_with_single_repetition_token(repetition_token):
    assert pygex.tokenize("a" + repetition_token) == ["a" + repetition_token]

@pytest.mark.parametrize("repetition_token", regex_repetition_tokens())
def test_tokenizer_throws_error_on_only_repetition_token(repetition_token):
    with pytest.raises(pygex.InvalidRegexPattern) as e:
        pygex.tokenize(repetition_token)
