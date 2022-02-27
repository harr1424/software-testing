def func(x):
    return x + 1

def test_func_faill():
    assert func(3) == 5

def test_func_pass():
    assert func(3) == 4


