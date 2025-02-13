# 1. Βασική Κλάση για τον Employee
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

# 2. Κλάση για τον Manager
class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# 3. Κλάση για τον Engineer
class Engineer(Employee):
    def __init__(self, name, employee_id, salary, specialization):
        super().__init__(name, employee_id, salary)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

# 4. Δοκιμή με είσοδο από τον χρήστη
# Παίρνουμε τα δεδομένα του χρήστη για Manager
print("Enter Manager Information:")
name_manager = input("Enter name: ")
employee_id_manager = input("Enter employee ID: ")
salary_manager = float(input("Enter salary: "))
department_manager = input("Enter department: ")

# Δημιουργία αντικειμένου Manager
manager = Manager(name_manager, employee_id_manager, salary_manager, department_manager)

# Παίρνουμε τα δεδομένα του χρήστη για Engineer
print("\nEnter Engineer Information:")
name_engineer = input("Enter name: ")
employee_id_engineer = input("Enter employee ID: ")
salary_engineer = float(input("Enter salary: "))
specialization_engineer = input("Enter specialization: ")

# Δημιουργία αντικειμένου Engineer
engineer = Engineer(name_engineer, employee_id_engineer, salary_engineer, specialization_engineer)

# Εκτύπωση των στοιχείων του Manager και του Engineer
print("\nManager Info:")
manager.display_info()

print("\nEngineer Info:")
engineer.display_info()
