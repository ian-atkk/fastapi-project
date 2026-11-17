"""Deliberately broken file for testing ruff and ty. Do not import this anywhere."""

import os  # ruff F401: unused import
import sys  # ruff F401: unused import


def add(a: int, b: int) -> int:
    unused = 42  # ruff F841: local variable assigned but never used
    return a + b


def get_name() -> str:
    return 123  # ty: returns int where str is declared


def check(value):
    if value is None:  # ruff SIM103: return the condition directly
        return True
    return False


result: int = add("1", "2")  # ty: str passed where int is expected
missing = add(1)  # ty: missing required argument `b`
length = len(5)  # ty: int has no __len__
upper = get_name().nonexistent()  # ty: str has no attribute `nonexistent`
print(undefined_variable)  # ruff F821 + ty: name is not defined
