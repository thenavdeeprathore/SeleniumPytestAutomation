import pytest


def test_m1():
    a = 10
    b = 11
    assert a + 1 == b, "test failed"
    assert a == b, "test failed as a is not equal to b"


def test_m2():
    name = "pytest"
    assert name.upper() == "PYTEST"


def test_m3():
    assert 1000 == 1000


# RUN: py.test
# This will execute all the tests (which are prefixed with test_) in all the classes (which are prefixed with test_)
