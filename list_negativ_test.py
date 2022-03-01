from negatives import list_add_neg, list_double_number, list_negativ_number, list_sum_number


def test_list_poz (): 
    numbers= ([1, 3, 4, 5, 6, 7])
    assert list_negativ_number(numbers) == 0

def test_list_null (): 
    # given, átadjuk a listát 
    numbers= ([])
    #when leellenőrizzük
    assert list_negativ_number(numbers) == 0

def test_list_negativ (): 
    numbers= ([1, 3, 4, 5, 6, 7, -2])
    assert list_negativ_number(numbers) > 0

def test_list_sum (): 
    numbers= ([1, 3, -2])
    assert list_sum_number(numbers) == 2 

def test_list_add_neg (): 
    numbers= ([1, 3, -2, -4])
    assert list_add_neg(numbers) == [-2, -4]

def test_list_double_number (): 
    numbers= ([1, 3, -2, -4])
    assert list_double_number(numbers) == [2, 6, -4, -8]