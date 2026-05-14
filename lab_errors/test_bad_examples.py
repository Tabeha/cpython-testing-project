from calculator import add, divide, multiply


SHARED_STATE: list[int] = []


def test_without_assert() -> None:
    add(2, 2)


def test_wrong_expected_value() -> None:
    assert add(2, 2) == 5


def test_too_weak_assertion() -> None:
    result = add(2, 2)
    assert result > 0


def test_missing_error_check() -> None:
    divide(10, 0)


def test_shared_mutable_state() -> None:
    SHARED_STATE.append(1)
    assert len(SHARED_STATE) == 1


def test_copy_paste_assertion() -> None:
    assert multiply(3, 4) == 11
