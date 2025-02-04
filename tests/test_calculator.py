'''My Calculator Test'''
from calculator import add

def test_addition():
    '''Test that addition function works'''
    assert add(2,2) == 4
