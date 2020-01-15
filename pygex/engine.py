#!/usr/bin/env python

from contextlib import suppress
from itertools import tee

class WildCardTransition:
    def valid_transition_character(self, character):
        return True

class SingleCharacterTransition:
    def __init__(self, character):
        self.character = character

    def valid_transition_character(self, character):
        return self.character == character

class State:
    @classmethod
    def end_state(cls):
        state = cls()
        state._end_state = True
        return state

    def __init__(self):
        self.transitions = []
        self._end_state = False

    def add_state_transition(self, character, transition_state):
        if character == '.':
            transition = WildCardTransition()
        else:
            transition = SingleCharacterTransition(character)

        self.transitions.append((transition, transition_state))

    def is_end_state(self):
        return self._end_state


def matches(string, pattern):
    start_state = compile(pattern)
    return state_match(string, start_state)

def state_match(string, start_state):
    if start_state.is_end_state():
        return True

    try:
        head, *tail = string
    except ValueError:
        return False

    for transition, state in start_state.transitions: #t ca*tt
        if transition.valid_transition_character(head) and state_match(tail, state):
            return True

    return False


def break_parts(pattern):
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


def compile(pattern): #.*c
    start_state = State()
    parts = break_parts(pattern)
    states = [start_state]
    for _ in range(len(parts)):
        states.append(State())
    #end_state = State.end_state()
    #states.append(end_state)


    parts_iter = iter(parts)
    states_iter = iter(states)

    for state in states[:-1]:
        parts_iter, next_parts = tee(parts_iter)

        next(states_iter)
        states_iter, next_states = tee(states_iter)

        add_transitions_to_state(state, next_parts, next_states)
        next(parts_iter)

    states[-1]._end_state = True

    return start_state


def add_transitions_to_state(state, parts, next_states):
    part = next(parts)#T
    next_state = next(next_states)#4
    with suppress(StopIteration):
        while part.endswith('*'):
            char = part[0]

            state.add_state_transition(char, next_state)
            next_state.add_state_transition(char, next_state)

            next_state = next(next_states)
            part = next(parts)


    state.add_state_transition(part, next_state)

