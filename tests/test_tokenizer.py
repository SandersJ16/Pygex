#!/usr/bin/env python

import pytest
from .. import pygex

def test_tokenizer_empty_string():
    assert pygex.tokenize("") == []

def test_tokenizer_no_special_characters():
    assert pygex.tokenize("abc") == ["a", "b", "c"]

def test_tokenizer_character_with_single_modifier():
    assert pygex.tokenize("a*") == ["a*"]
    assert pygex.tokenize("b+") == ["b+"]
    assert pygex.tokenize("c?") == ["c?"]
