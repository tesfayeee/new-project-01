class Employee:  # this is the parent class
    def __init__(self, name, emp_ID):
        self.name = name
        self.emp_id = emp_ID
    def display_info(self):

        print("Employee Nmae :" , self.name) # printing the employent
        print("Employee_ Id", self.emp_id )

        #class subclass 01
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_Id,salary):
        super().__init__(name, emp_Id)
        self.salary = salary

        #override the display info Method 
    def display_info(self):
        super().display_info()
        print("Employee salary :", self.salary)

# sub|class 02
class PartTimeEmploye(Employee):
    def __init__(self,name,emp_Id, hourly_rate, hourly_worked):
        super().__init__(self,name, emp_Id,)
        self.hourly_rate = hourly_rate
        self.hourl_worked = hourly_worked
        
# overrided the disply info method
    def display_info():
        super().display_info()             # called the parent name [ display info]
        print("hourly Rate: ",self.hourly_rate ):       #printed the remainig attributes _Hourly Rate
        print("hour worked :", self.hourly_worked ):      #printed the remainig attributes_hourly worked






# COPIED PAGE (YAADANNOO CODE KANAA) FROM NOTE BOOK


# class Employee:  # Parent class
    def __init__(self, name, emp_Id):
        self.name = name
        self.emp_id = emp_Id

    def display_info(self):
        print("Employee Name:", self.name)  # Fixed typo
        print("Employee ID:", self.emp_id)  # Fixed typo

# Subclass 01
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_Id, salary):
        super().__init__(name, emp_Id)
        self.salary = salary

    # Overriding the display_info method
    def display_info(self):
        super().display_info()
        print("Employee Salary:", self.salary)

# Subclass 02
class PartTimeEmployee(Employee):  # Fixed typo in class name
    def __init__(self, name, emp_Id, hourly_rate, hours_worked):  # Fixed constructor
        super().__init__(name, emp_Id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked  # Fixed variable name

    # Overriding the display_info method
    def display_info(self):
        super().display_info()
        print("Hourly Rate:", self.hourly_rate)
        print("Hours Worked:", self.hours_worked)  # Fixed variable name

# Example usage:
full_time = FullTimeEmployee("John Doe", "FT001", 50000)
part_time = PartTimeEmployee("Jane Smith", "PT001", 20, 25)

full_time.display_info()
print()
# part_time.display_info()

# 




# YAADANNOO DATA input Gochuuf  CODE ASIIN OLII SANA



class Employee:  # Parent class
    def __init__(self, name, emp_Id):
        self.name = name
        self.emp_id = emp_Id

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)

# Subclass 01
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_Id, salary):
        super().__init__(name, emp_Id)
        self.salary = salary

    # Overriding the display_info method
    def display_info(self):
        super().display_info()
        print("Employee Salary:", self.salary)

# Subclass 02
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_Id, hourly_rate, hours_worked):
        super().__init__(name, emp_Id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Overriding the display_info method
    def display_info(self):
        super().display_info()
        print("Hourly Rate:", self.hourly_rate)
        print("Hours Worked:", self.hours_worked)

# Function to get user input and create an employee
def create_employee():
    employee_type = input("Enter employee type (full-time/part-time): ").lower()

    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")

    if employee_type == "full-time":
        salary = float(input("Enter salary: "))
        emp = FullTimeEmployee(name, emp_id, salary)
    elif employee_type == "part-time":
        hourly_rate = float(input("Enter hourly rate: "))
        hours_worked = float(input("Enter hours worked: "))
        emp = PartTimeEmployee(name, emp_id, hourly_rate, hours_worked)
    else:
        print("Invalid employee type")
        return None

    return emp

# Main code to create and display employee info
employee = create_employee()
if employee:
    employee.display_info()