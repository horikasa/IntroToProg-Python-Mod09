# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudocode to start assignment 9
# HOrikasa,12.13.2021,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

# Import modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported.")

# Data
emp_file = 'EmployeeData.txt'
lst_table = []

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
temp_list = Fp.read_data_from_file(emp_file)
for row in temp_list:
    lst_table.append(Emp(row[0], row[1], row[2].strip()))

while True:
    Eio.print_menu_items()  # Show user a menu of options
    strChoice = Eio.input_menu_options()  # Get user's menu option choice

    if strChoice == '1':  # Show user current data in the list of employee objects
        Eio.print_current_list_items(lst_table)
        continue
    elif strChoice == '2':  # Let user add data to the list of employee objects
        new_emp = Eio.input_employee_data()
        lst_table.append(new_emp)
        continue
    elif strChoice == '3':  # let user save current data to file
        Fp.save_data_to_file(emp_file, lst_table)
        print("Data has been saved!")
        continue
    elif strChoice == '4':  # Let user exit program
        print("See you next time!")
        break
