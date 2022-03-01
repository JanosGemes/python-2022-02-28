numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
evens = [6, 8, 10]

names = ["Jack Doe", "Jhon Doe", "Jane Doe"]

employee = ["Jack Doe", 30]

for number in numbers:
    print(number)

print(names[2])

names[2] = "Jane Smith"
print(names)

names.append("John Smith")
print(names)

dogs = []
print(dogs)
dogs.append("Morzsi")
print(dogs)

print(names[1:3])
print(names[1:3:2])
print(names[1:])
print(names[1:3:-1])
print(names[::-1])

#számlálás tétele
count = 0
for number in numbers:
    if number % 2 == 0:
        count +=1
print(count)

def 