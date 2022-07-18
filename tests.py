from src.ezlambda import _, _m  # type: ignore

def test_repr():
    assert repr(_) == "_(None)"
    assert repr(_.upper(_m)) == "_(f = __call__, p = (), c = _(f = __getattribute__, p = ('upper',), c = _(None)))"

def test_chaining():
    assert list(map(_.upper(_m), ["apple", "banana", "cherry"])) == ['APPLE', 'BANANA', 'CHERRY']
    assert list(map(_.__class__.__name__.upper(_m), [1, "a", True, []])) == ['INT', 'STR', 'BOOL', 'LIST']

if __name__ == '__main__':
    pass
