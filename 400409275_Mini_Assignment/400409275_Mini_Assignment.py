'''
Teghveer Ateliey
atelieyt
400409275
April 6, 2022
'''

from Guest_class import Guest

def park_expenses(num_employees, wage, num_rides):
    hours = 8
    operational_costs = 10000
    expenses = num_employees * wage * hours + num_rides * operational_costs
    return expenses

def revenue_and_profit(expenses, gross_margin_percent):
    required_revenue = expenses / (1 - gross_margin_percent)
    gross_profit = required_revenue - expenses
    return [required_revenue, gross_profit]

def create_guests(guest_attributes):
    new_guest = Guest(guest_attributes[0], guest_attributes[1])
    new_guest.set_stamina(guest_attributes[2])
    new_guest.set_hunger(guest_attributes[3])
    new_guest.set_money_spent()
    return new_guest

def main():
    START_UP = 1000000.0
    NUM_RIDES = 15
    NUM_EMPLOYEES = 250
    WAGE = 25
    GROSS_MARGIN_PERCENT = 0.2
    
    expenses = park_expenses(NUM_EMPLOYEES, WAGE, NUM_RIDES)
    print(expenses)
    
    daily_income = revenue_and_profit(expenses, GROSS_MARGIN_PERCENT)
    print(daily_income[0], GROSS_MARGIN_PERCENT)
    
    gross_total_profit = daily_income[1]
    day = 1
    print("Gross Profit\tDay #")
    
    while(gross_total_profit <= START_UP):
        print(round(gross_total_profit, 2), "\t", day)
        day += 1
        gross_total_profit += revenue_and_profit(expenses, GROSS_MARGIN_PERCENT)[1]
        
    guest_1 = create_guests(["active guest", 500, 10, 4])
    guest_2 = create_guests(["hungry guest", 500, 4, 7])
    
    if(guest_1.get_money_spent() > guest_2.get_money_spent()):
        print(guest_1.get_name(), guest_1.get_money_spent())
    elif(guest_1.get_money_spent() < guest_2.get_money_spent()):
        print(guest_2.get_name(), guest_2.get_money_spent())
    else:
        print(guest_1.get_name(), guest_1.get_money_spent())
        print(guest_2.get_name(), guest_2.get_money_spent())
        
    guest_file = open("guest_list.txt", "r")
    guest_attributes = guest_file.readlines()
    guest_file.close()
    
    for line in guest_attributes:
        split_str = line.split()
        guest = []
        guest.append(split_str[0])
        for i in range(1, 4):
            guest.append(int(split_str[i]))
        new_guest = create_guests(guest)
        print(new_guest.get_name() + " will spend $" + str(round(new_guest.get_money_spent(), 2)) + " at the park.")
