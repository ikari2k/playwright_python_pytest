from test_pytest_basic_tuples import Task


def test_asdict():
    t_task = Task("do something", "Jack", True, 21)
    t_dict = t_task._asdict()
    expected = {"summary": "do something", "owner": "Jack", "done": True, "id": 21}
    assert t_dict == expected


def test_replace():
    t_before = Task("finish work", "Jack", False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task("finish work", "Jack", True, 10)
    assert t_after == t_expected
