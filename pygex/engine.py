#!/usr/bin/env python

from contextlib import suppress

def matches(string, pattern):
    parts = _compile(pattern)
    string_counter = 0

    for part in parts:
        if part.endswith('*'):
            char = part[0]
            while string_counter < len(string) and string[string_counter] == char:
                string_counter += 1
        else:
            if string_counter >= len(string) or (part != string[string_counter] and part != '.'):
                return False
            string_counter += 1
    return True



def _compile(pattern):
    parts = []

    pattern_iter = iter(pattern)
    last_part = None
    while True:
        try:
            part = next(pattern_iter)
            if part == "*":
                parts.append(last_part + part)
            elif last_part != "*" and last_part is not None:
                parts.append(last_part)
            last_part = part
        except StopIteration:
            if last_part != "*" and last_part is not None:
                parts.append(last_part)
            break

    return parts
