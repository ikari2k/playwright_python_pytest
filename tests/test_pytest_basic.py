def test_pass():
    assert (3, 4, 5) == (3, 4, 5)


def test_fail():
    assert (3, 4, 5) == (1, 2, 3)
