from implem3 import in_set


def test_in():
    assert in_set(3, {2, 4, 7, 3, 9})
    assert in_set(4, {5, 7, 9, 4, 3})


def test_out():
    assert in_set(2, {8, 9, 6, 4}) == False
    assert in_set(5, {8, 7, 6, 1}) == False


