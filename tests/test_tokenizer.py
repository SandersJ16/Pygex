#!/usr/bin/env python

import pytest
from .. import pygex

def test_tokenizer_no_special_characters():
    assert pygex.tokenize("abc") == ["a", "b", "c"]

