#!/usr/bin/env python

special_character = ["^", ".", "[", "]", "$", "(", ")", "\\", "*", "{", "}", "?", "+", "|"]
repetition_tokens = ["*", "?", "+"]

def tokenize(pattern):
    tokens = []
    for part in pattern:
        if part in repetition_tokens:
            tokens[-1] += part
        else:
            tokens.append(part)

    return tokens




