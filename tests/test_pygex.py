#!/usr/bin/env python

import pytest
from ..pygex.engine import Engine

def test_literal_string_matches():
    assert Engine.matches('cat', 'cat')

def test_literal_string_match_failure():
    assert not Engine.matches('cat', 'hat')

def test_literal_match_failure_different_case():
    assert not Engine.matches('cat', 'cAt')

def test_pattern_with_wildcard():
    assert Engine.matches('cat', 'c.t')
    assert Engine.matches('cat', '.at')

