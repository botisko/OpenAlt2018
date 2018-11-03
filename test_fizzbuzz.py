import pytest
import math
from fz import fizzbuzz


def test_fizzbuzz_takes_number_returns_str():
    assert isinstance(fizzbuzz(1), str)


@pytest.mark.parametrize(('number', 'expected'),[(1, '1'),(2, '2'),(4, '4'),(7, '7')])
def test_fizzbuzz_regular_returns_numbers(number, expected):
    assert fizzbuzz(number) == expected


@pytest.mark.parametrize('fizzes',[3,6,9,12,18,21])
def test_fizzbuzz_fizzes_returns_fizz(fizzes):
    assert fizzbuzz(fizzes) == 'fizz'


@pytest.mark.parametrize('buzzes',[5,10,20,25,35])
def test_fizzbuzz_buzzes_returns_buzz(buzzes):
    assert fizzbuzz(buzzes) == 'buzz'


@pytest.mark.parametrize('fizzbuzzes',[15,30,300])
def test_fizzbuzz_returns_fizzbuzz(fizzbuzzes):
    assert fizzbuzz(fizzbuzzes) == 'fizzbuzz'


def test_cannot_fizzbuzz_strs():
    with pytest.raises(TypeError):
        fizzbuzz("nope")


def test_cannot_fizzbuzz_none():
    with pytest.raises(TypeError):
        fizzbuzz(None)


def test_cannot_fizzbuzz_none():
    with pytest.raises(TypeError):
        fizzbuzz(5.5)

### TEST DO BUDOUCNA, ZATIM NEFUNKCNI FUNKCIONALITA ATD ###
@pytest.mark.xfail
def test_xxx():
    assert False
