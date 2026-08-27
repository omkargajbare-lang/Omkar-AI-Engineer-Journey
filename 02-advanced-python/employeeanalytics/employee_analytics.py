from abc import ABC, abstractmethod


# ============================================================
# Performance Review
# Demonstrates Composition
# Employee HAS-A PerformanceReview
# ============================================================

class PerformanceReview:

    def __init__(self, rating, comments):
        self.rating = rating
        self.comments = comments

    def __str__(self):
        return f"Rating: {self.rating} | {self.comments}"


# ============================================================
# Employee
# Demonstrates:
# - Abstraction
# - Encapsulation
# - Instance variables
# - Constructor
# - Methods
# ============================================================

class Employee(ABC):

    def __init__(self, name, salary, department, performance_review=None):
        self.name = name
        self.salary = salary
        self.department = department
        self.performance_review = performance_review

    # --------------------------------------------------------
    # Encapsulation using @property
    # --------------------------------------------------------

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    # --------------------------------------------------------
    # String representation of Employee object
    # --------------------------------------------------------

    def __str__(self):
        return f"{self.name} | {self.salary} | {self.department}"

    # --------------------------------------------------------
    # Employee validation
    # --------------------------------------------------------

    def validate(self):
        errors = []

        if self.salary <= 0:
            errors.append({
                "employee": self.name,
                "error_type": "InvalidSalary",
                "message": "Salary must be greater than 0"
            })

        if not self.name:
            errors.append({
                "employee": self.name,
                "error_type": "InvalidName",
                "message": "Employee name cannot be empty"
            })

        if not self.department:
            errors.append({
                "employee": self.name,
                "error_type": "InvalidDepartment",
                "message": "Department cannot be empty"
            })

        return errors

    # --------------------------------------------------------
    # Abstraction
    # Every Employee type must implement this method.
    # --------------------------------------------------------

    @abstractmethod
    def calculate_total_compensation(self):
        pass


# ============================================================
# Manager
# Demonstrates Inheritance
# Manager IS-A Employee
# ============================================================

class Manager(Employee):

    def __init__(
        self,
        name,
        salary,
        department,
        bonus,
        performance_review=None
    ):
        super().__init__(
            name,
            salary,
            department,
            performance_review
        )

        self.bonus = bonus

    def calculate_total_compensation(self):
        return self.salary + self.bonus


# ============================================================
# Contractor
# Demonstrates Inheritance
# Contractor IS-A Employee
# ============================================================

class Contractor(Employee):

    def __init__(
        self,
        name,
        salary,
        department,
        contract_bonus,
        performance_review=None
    ):
        super().__init__(
            name,
            salary,
            department,
            performance_review
        )

        self.contract_bonus = contract_bonus

    def calculate_total_compensation(self):
        return self.salary + self.contract_bonus


# ============================================================
# Employee Validator
# Responsible for validating Employee objects.
# ============================================================

class EmployeeValidator:

    def __init__(self, employees):
        self.employees = employees

    def validate(self):

        valid_employees = []
        invalid_employees = []
        errors = []

        print("Validation Process Started...")

        for employee in self.employees:

            employee_errors = employee.validate()

            if not employee_errors:
                valid_employees.append(employee)

            else:
                invalid_employees.append(employee)
                errors.extend(employee_errors)

        return valid_employees, invalid_employees, errors


# ============================================================
# Employee Analytics
# Responsible for analyzing valid employees.
# ============================================================

class EmployeeAnalytics:

    def __init__(self, valid_employees):
        self.valid_employees = valid_employees

    # --------------------------------------------------------
    # Employee count
    # --------------------------------------------------------

    def count_employees(self):
        return len(self.valid_employees)

    # --------------------------------------------------------
    # Salary analytics
    # --------------------------------------------------------

    def calculate_total_salary(self):

        total_salary = 0

        for employee in self.valid_employees:
            total_salary += employee.salary

        return total_salary

    def calculate_average_salary(self):

        if not self.valid_employees:
            return 0

        return (
            self.calculate_total_salary()
            / len(self.valid_employees)
        )

    def find_highest_salary(self):

        if not self.valid_employees:
            return 0

        highest_salary = self.valid_employees[0].salary

        for employee in self.valid_employees:

            if employee.salary > highest_salary:
                highest_salary = employee.salary

        return highest_salary

    def find_lowest_salary(self):

        if not self.valid_employees:
            return 0

        lowest_salary = self.valid_employees[0].salary

        for employee in self.valid_employees:

            if employee.salary < lowest_salary:
                lowest_salary = employee.salary

        return lowest_salary

    # --------------------------------------------------------
    # Highest / Lowest paid employee
    # --------------------------------------------------------

    def find_highest_paid_employee(self):

        if not self.valid_employees:
            return None

        highest_employee = self.valid_employees[0]

        for employee in self.valid_employees:

            if employee.salary > highest_employee.salary:
                highest_employee = employee

        return highest_employee

    def find_lowest_paid_employee(self):

        if not self.valid_employees:
            return None

        lowest_employee = self.valid_employees[0]

        for employee in self.valid_employees:

            if employee.salary < lowest_employee.salary:
                lowest_employee = employee

        return lowest_employee

    # --------------------------------------------------------
    # Department analytics
    # --------------------------------------------------------

    def analyze_departments(self):

        department_data = {}

        for employee in self.valid_employees:

            department = employee.department

            if department not in department_data:

                department_data[department] = {
                    "count": 0,
                    "total_salary": 0,
                    "average_salary": 0
                }

            department_data[department]["count"] += 1

            department_data[department]["total_salary"] += (
                employee.salary
            )

            department_data[department]["average_salary"] = (
                department_data[department]["total_salary"]
                / department_data[department]["count"]
            )

        return department_data

    # --------------------------------------------------------
    # Compensation analytics
    # Demonstrates Polymorphism
    # --------------------------------------------------------

    def calculate_total_compensation(self):

        total_compensation = 0

        for employee in self.valid_employees:
            total_compensation += (
                employee.calculate_total_compensation()
            )

        return total_compensation


# ============================================================
# Sample Employee Data
# ============================================================

def create_employees():

    return [
        Manager(
            "Rahul",
            50000,
            "IT",
            10000,
            PerformanceReview(
                4.5,
                "Excellent technical performance"
            )
        ),

        Manager(
            "",
            70000,
            "HR",
            15000
        ),

        Contractor(
            "Chetan",
            0,
            "IT",
            5000
        ),

        Contractor(
            "Danish",
            -200,
            "Finance",
            3000
        ),

        Manager(
            "Eknath",
            20000,
            "IT",
            5000
        ),

        Manager(
            "Farukh",
            70000,
            "HR",
            12000
        ),

        Contractor(
            "Gunjan",
            10000,
            "Finance",
            2000
        ),

        Contractor(
            "Haripriya",
            -2200,
            "IT",
            1000
        ),

        Manager(
            "Indu",
            92000,
            "Finance",
            20000,
            PerformanceReview(
                5,
                "Outstanding performance"
            )
        ),

        Manager(
            "Janhavi",
            60200,
            "HR",
            10000
        )
    ]


# ============================================================
# Display Helpers
# ============================================================

def display_employee_list(title, employees):

    print(f"\n{title}")

    if not employees:
        print("None")
        return

    for employee in employees:
        print(employee)


def display_errors(errors):

    print("\nValidation Errors:")

    if not errors:
        print("No validation errors found.")
        return

    for error in errors:

        print(
            f"{error['employee']} | "
            f"{error['error_type']} | "
            f"{error['message']}"
        )


# ============================================================
# Main Application
# ============================================================

def main():

    # --------------------------------------------------------
    # 1. Create employees
    # --------------------------------------------------------

    employees = create_employees()

    display_employee_list(
        "Original Employee List:",
        employees
    )

    # --------------------------------------------------------
    # 2. Validate employees
    # --------------------------------------------------------

    validator = EmployeeValidator(employees)

    (
        valid_employees,
        invalid_employees,
        errors
    ) = validator.validate()

    display_employee_list(
        "Valid Employees:",
        valid_employees
    )

    display_employee_list(
        "Invalid Employees:",
        invalid_employees
    )

    display_errors(errors)

    # --------------------------------------------------------
    # 3. Create analytics object
    # --------------------------------------------------------

    analytics = EmployeeAnalytics(valid_employees)

    # --------------------------------------------------------
    # 4. Employee counts
    # --------------------------------------------------------

    print("\nEmployee Count:")

    print(
        "Valid Employees:",
        analytics.count_employees()
    )

    print(
        "Invalid Employees:",
        len(invalid_employees)
    )

    print(
        "Total Employees:",
        len(employees)
    )

    # --------------------------------------------------------
    # 5. Salary analytics
    # --------------------------------------------------------

    print("\nSalary Analytics:")

    print(
        "Total Salary:",
        analytics.calculate_total_salary()
    )

    print(
        "Average Salary:",
        analytics.calculate_average_salary()
    )

    print(
        "Highest Salary:",
        analytics.find_highest_salary()
    )

    print(
        "Lowest Salary:",
        analytics.find_lowest_salary()
    )

    # --------------------------------------------------------
    # 6. Highest / Lowest paid employee
    # --------------------------------------------------------

    highest_paid = (
        analytics.find_highest_paid_employee()
    )

    lowest_paid = (
        analytics.find_lowest_paid_employee()
    )

    print("\nHighest Paid Employee:")
    print(highest_paid)

    print("\nLowest Paid Employee:")
    print(lowest_paid)

    # --------------------------------------------------------
    # 7. Department analytics
    # --------------------------------------------------------

    department_data = analytics.analyze_departments()

    print("\nDepartment Analytics:")

    for department, data in department_data.items():

        print(
            f"{department} | "
            f"Employees: {data['count']} | "
            f"Total Salary: {data['total_salary']} | "
            f"Average Salary: {data['average_salary']:.2f}"
        )

    # --------------------------------------------------------
    # 8. Total compensation
    # --------------------------------------------------------

    print("\nTotal Compensation:")

    print(
        analytics.calculate_total_compensation()
    )

    # --------------------------------------------------------
    # 9. Performance reviews
    # --------------------------------------------------------

    print("\nPerformance Reviews:")

    for employee in valid_employees:

        if employee.performance_review:

            print(
                f"{employee.name} | "
                f"{employee.performance_review}"
            )

    print("\nProcess Complete!")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()