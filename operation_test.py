from operations import add


def test_add():
    #given kitaláljuk a bemenő paramétereket

    x = 5
    y = 10
    #when elvégezzük a függvényt
    result = add(x,y)
    #then összehasonlítás assert el
    assert result == 15

def test_add_simple():
    assert add (5, 10) == 15