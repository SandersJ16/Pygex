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
    assert pygex.matches('cat', 'ca.')

def test_pattern_with_asteriks_matches_none():
    assert pygex.matches('ct', 'ca*t')

def test_pattern_with_asteriks_and_extra_charachter_doesnt_match():
    assert not pygex.matches('ct', 'ca*tt')

def test_patterns_with_asteriks_matches_one():
    assert pygex.matches('cat', 'ca*t')

def test_patterns_with_asteriks_matches_multiple():
    assert pygex.matches('caaat', 'ca*t')

def test_patterns_with_asteriks_matches_with_following_matching_character():
    assert pygex.matches('cat', 'ca*at')

