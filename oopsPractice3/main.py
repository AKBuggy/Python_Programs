class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, emp_id, emp_salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.emp_salary = emp_salary


def main():
    employee = Employee("Ankit", 21, 123, 600000)
    print(f'Employee name: {employee.name}')
    print(f'Employee age: {employee.age}')
    print(f'Employee id: {employee.emp_id}')
    print(f'Employee salary: {employee.emp_salary}')


if __name__ == '__main__':
    main()
