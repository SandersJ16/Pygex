#!/usr/bin/env python

def matches(string, pattern):
    for string_char, pattern_char in zip(string, pattern):
        if pattern_char != '.' and pattern_char != string_char:
            return False
    return True


