from calculator import add, divide


def test_without_assert():
    add(2, 2)


def test_wrong_expected_value():
    assert add(2, 2) == 5


def test_too_weak_assertion():
    result = add(2, 2)
    assert result > 0


def test_missing_error_check():
    divide(10, 0)