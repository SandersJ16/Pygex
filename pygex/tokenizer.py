#!/usr/bin/env python

special_character = ["^", ".", "[", "]", "$", "(", ")", "\\", "*", "{", "}", "?", "+", "|"]
repetition_tokens = ["*", "?", "+"]

def tokenize(pattern):
    tokens = []
    for part in pattern:
        if part in repetition_tokens:
            try:
                tokens[-1] += part
            except IndexError:
                raise InvalidRegexPattern()
        else:
            tokens.append(part)

    return tokens



class InvalidRegexPattern(Exception):
    pass
