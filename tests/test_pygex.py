#!/usr/bin/env python

import pytest
from ..pygex import Engine

def test_basic():
    assert Engine.matches('a', 'a') is True
