from src.ezlambda import _, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, _m, Var, VarMarker  # type: ignore

def test_repr():
    assert repr(_) == "_"
    assert repr(_.upper(_m)) == "((_ get 'upper') call ())"

def test_chaining():
    assert list(map(_.upper(_m), ["apple", "banana", "cherry"])) == ['APPLE', 'BANANA', 'CHERRY']
    assert list(map(_.__class__.__name__.upper(_m), [1, "a", True, []])) == ['INT', 'STR', 'BOOL', 'LIST']
    assert list(map(a ** 2 + b * b - c ** 2, [i * 3 for i in range(10)], [i * 4 for i in range(10)], [i * 5 for i in range(10)])) == [0] * 10

if __name__ == '__main__':
    print((x * (2 + y))(5, 3))
    print(list(map(_.upper(_m), ["apple", "banana", "cherry"])))
    print(list(map(_.__class__.__name__.upper(_m), [1, "a", True, []])))
    print(list(map(a ** 2 + b * b - c ** 2, [i * 3 for i in range(10)], [i * 4 for i in range(10)], [i * 5 for i in range(10)])))
