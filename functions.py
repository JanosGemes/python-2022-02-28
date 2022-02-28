def print_employee_data(name: str, age: int, repeat: int = 5, log: bool = False):
    for i in range(0, repeat):
        base_employee_data = ""
        if log:
            base_employee_data = base_employee_data + f"{i + 1} "
        base_employee_data = base_employee_data + f"{name} {age} "
        print(f"{base_employee_data}")


print("Begin")
print_employee_data("John Doe", 30, True)
print("End")
print_employee_data("Más", 40)
print("End")

print_employee_data(age=60, name="John Smith", log=True)

print_employee_data(100, "Szoveg")
