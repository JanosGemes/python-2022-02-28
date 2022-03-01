
#számlálás tétele
def list_negativ_number(numbers):
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return  count

#összegzés tétele
def list_sum_number(numbers):
    sum = 0
    for number in numbers:
        sum += number 
    return  sum
#szűrés tétele
def list_add_neg(numbers):
    result = []
    for number in numbers:
         if number < 0:
             result.append(number)
    return result

# transzformáció
def list_double_number(numbers):
    result = []
    for number in numbers:
         result.append(number*2)
    return result