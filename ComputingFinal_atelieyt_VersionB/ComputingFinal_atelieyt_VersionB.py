'''
Teghveer Ateliey
atelieyt
400409275
Version B
April 7, 2022
'''

from Employee_class import Employee

# determines employee's salary and how much of their income is alloted
# to each expense
def income_allotment(salary):
    # confirms salary is a float, initiates tax_rate and calculates income after tax
    salary = float(salary)
    TAX_RATE = 0.30
    monthly_after_tax = (salary * (1 - TAX_RATE)) / 12
    
    # determines income allotment for savings, needs, and wants based on income after tax
    savings  = 0.2 * monthly_after_tax
    needs = 0.5 * monthly_after_tax
    wants = 0.3 * monthly_after_tax
    
    # returns savings, needs, and wants in a 3 item list
    return [savings, needs, wants]

# determines mortgage of person and returns that value as float
def calc_mortgage_principal(lending_rate, num_years, monthly_mortgage_payments):
    # confirms that each of the arguments are their proper types
    lending_rate = float(lending_rate)
    num_years = int(num_years)
    monthly_mortgage_payments = float(monthly_mortgage_payments)
    
    # calculates the monthly lending rate and number of months until mortgage is paid off
    monthly_lending_rate = lending_rate / 12
    num_months = num_years * 12
    
    # calculates and returns mortgage using equation (2)
    mortgage = monthly_mortgage_payments*(((1+monthly_lending_rate)**num_months-1)/(monthly_lending_rate*(1+monthly_lending_rate)**num_months))
    return mortgage

# calculates and returns total contribution to pension from employee and employer as float
def annual_pension_contribution(salary):
    # Initiates deduction rate as constant and confirms salary is a float
    salary = float(salary)
    DEDUCTION_RATE = 0.05
    
    # calculates deduction rate using equation (3)
    deduction = salary * DEDUCTION_RATE
    
    # assigns match_factor based on salary of individual in increments of 2.5, 2.0, and 1.0 as salary increases
    if(salary < 100000):
        match_factor = 2.5
    elif(100000 <= salary < 200000):
        match_factor = 2.0
    else:
        match_factor = 1.0
    
    # calculates match from employer and calulates and returns total contribution
    match = deduction * match_factor
    total_contribution = deduction + match
    return total_contribution

# main function which utilizes Employees class and all functions and returns all calculated values
def main():
    # intiates base salary, prime_rate, and num_years variables for later calculations
    SALARY = float(175000)
    PRIME_RATE = 0.039
    NUM_YEARS = 25
    
    # calculates income after tax from salary using income_allotment function
    income_after_tax = income_allotment(SALARY)
    # print each value from list for allotted income on a new line
    print("After-tax income allotted towards 'savings' is $" + str(round(income_after_tax[0],2)))
    print("After-tax income allotted towards 'needs' is $" + str(round(income_after_tax[1],2)))
    print("After-tax income allotted towards 'wants' is $" + str(round(income_after_tax[2],2)))
    
    # calculates lending rate from bank
    lending_rate = PRIME_RATE - 0.005
    # calculates monthly_mortgage_payments as 40% of the income allotted to needs
    monthly_mortgage_payments = 0.4 * income_after_tax[1]
    # calculates mortgage principal from the function dedicated to calculating it
    mortage_principal = calc_mortgage_principal(lending_rate, NUM_YEARS, monthly_mortgage_payments)
    
    # calculates total mortgage payments using monthly payments multiplied by number of months
    total_mortgage_payments = monthly_mortgage_payments * (NUM_YEARS * 12)
    # calulates total interest paid on mortgage
    total_interest_paid = total_mortgage_payments - mortage_principal
    
    # returns values that have been calculated
    print("The principal of your mortgage will be $" + str(round(mortage_principal, 2)))
    print("Over", NUM_YEARS, "years, $" + str(round(total_interest_paid, 2)) + " will be paid in interest.")
    # states if total interest paid is greater or less than half of mortage principal
    if (total_interest_paid / mortage_principal) < 0.5:
        print("the interest paid is less than half of the mortgage principal")
    else:
        print("the interest paid is greater than half of the mortgage principal")
       
    # calculates the pension for our base salary after 25 years
    # prints the pension after each yearly calculation
    pension = float(0)
    # calculates gain
    gain = PRIME_RATE + 0.01
    # iterates for each year which will be 25 times
    for i in range(NUM_YEARS):
        # calculates total contribution using the contribution function
        total_contribution = annual_pension_contribution(SALARY)
        # calculates pension using equation (7) and prints the value rounded to 2 decimals
        pension = (pension + total_contribution) * (1+gain)
        print("After", i+1, "year, the pension value will be $" + str(round(pension, 2)))
    # saves pension value to return later
    final_pension = pension
    
    # intiates all 3 employees with Employee class
    employ_1 = Employee("Karlo", SALARY - 120000)
    employ_2 = Employee("Hosam", SALARY + 50000)
    employ_3 = Employee("Mostafa", SALARY)
    
    # calculates the number of years for Karlo's pension to exceed 2 million
    pension = 0.0
    years = 0
    # iterates while pension is less than 2 million
    while pension < 2000000:
        # calculates total contribution using the contribution function
        total_contribution = annual_pension_contribution(employ_1.get_salary())
        # calculates pension using equation (7) and prints the value rounded to 2 decimals
        pension = (pension + total_contribution) * (1+gain)
        years += 1
    # prints number of years it will take and saves values calculated to return later
    print("It will take", years, "years for Karlo to accumulate a pension totalling $" + str(round(pension, 2)))
    employ_1_years = round(years, 2)
    employ_1_pension = round(pension, 2)
    
    # calculates the number of years for Hosam's pension to exceed 2 million
    pension = 0.0
    years = 0
    # iterates while pension is less than 2 million
    while pension < 2000000:
        # calculates total contribution using the contribution function
        total_contribution = annual_pension_contribution(employ_2.get_salary())
        # calculates pension using equation (7) and prints the value rounded to 2 decimals
        pension = (pension + total_contribution) * (1+gain)
        years += 1
    # prints number of years it will take and saves values calculated to return later
    print("It will take", years, "years for Hosam to accumulate a pension totalling $" + str(round(pension, 2)))
    employ_2_years = round(years, 2)
    employ_2_pension = round(pension, 2)
    
    # calculates the number of years for Mostafa's pension to exceed 2 million
    pension = 0.0
    years = 0
    # iterates while pension is less than 2 million
    while pension < 2000000:
        # calculates total contribution using the contribution function
        total_contribution = annual_pension_contribution(employ_3.get_salary())
        # calculates pension using equation (7) and prints the value rounded to 2 decimals
        pension = (pension + total_contribution) * (1+gain)
        years += 1
    # prints number of years it will take and saves values calculated to return later
    print("It will take", years, "years for Mostafa to accumulate a pension totalling $" + str(round(pension, 2)))
    employ_3_years = round(years, 2)
    employ_3_pension = round(pension, 2)
    
    # returns literally every value calculated in a list of lists
    return [[round(income_after_tax[0],2), round(income_after_tax[1],2), round(income_after_tax[2],2)], 
            [round(mortage_principal, 2), round(total_interest_paid, 2)], 
            [round(final_pension, 2)],
            [employ_1_years, employ_1.get_name(), employ_1_pension],
            [employ_2_years, employ_2.get_name(), employ_2_pension],
            [employ_3_years, employ_3.get_name(), employ_3_pension]]
