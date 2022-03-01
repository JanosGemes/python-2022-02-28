from newgit import number_15


def test_larger_with_big_number():
    # Given (Nincs most mit előkészíteni)
    # When (meghívjuk a fv-t)
    result = number_15(100)
    # Then
    assert result == True


def test_low_with_big_number():
    # Given (Nincs most mit előkészíteni)
    # When (meghívjuk a fv-t)
    result = number_15(2)
    # Then
    assert result == False

def test_neg_with_big_number():
    # Given (Nincs most mit előkészíteni)
    # When (meghívjuk a fv-t)
    result = number_15(-2)
    # Then
    assert result == False

def test_eq_with_big_number():
    # Given (Nincs most mit előkészíteni)
    # When (meghívjuk a fv-t)
    result = number_15(15)
    # Then
    assert result == False