#!/usr/bin/env python

import pytest
from .. import pygex

def test_literal_string_matches():
    assert pygex.matches('cat', 'cat')

def test_literal_string_match_failure():
    assert not pygex.matches('cat', 'hat')

def test_literal_match_failure_different_case():
    assert not pygex.matches('cat', 'cAt')

def test_pattern_with_wildcard():
    assert pygex.matches('cat', 'c.t')
    assert pygex.matches('cat', '.at')

def test_pattern_with_asteriks_matches_none():
    assert pygex.matches('ct', 'ca*t')

