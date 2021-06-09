
from example_python_package_shim import multi


def test_multi_with_small_numbers():

    answer = multi(3, 3)

    assert answer == 9


def test_multi_with_big_numbers():

    answer = multi(100, 2)

    assert answer == 200
