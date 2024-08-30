# Jarod Lopez / November 30, 2023 / Computers & Programming I Section 4 / Chapter 6 Assignment
# jel250@scarletmail.rutgers.edu
print("Jarod Lopez / November 30, 2023 / Computers & Programming I Section 4 / Chapter 6 Assignment")
print("jel250@scarletmail.rutgers.edu")

import random
import datetime
KNIVES = 10.0
LADELS = 3.0
SAUCE_PANS = 12.0
TAX_RATE = 0.07

def kitchenware_order():
    proceed = 'y'
    print("Welcome to Jarod's Kitchenware Shop!")
    while proceed == 'y':
        print(f"Knives are ${KNIVES:.2f}. We have 8 knives left.")
        knives_count = int(input("Enter the number of knives you would like: "))
        while knives_count <= 0 or knives_count > 8:
            print("Error: Please enter an appropriate answer (Do not enter zero, a negative number, or exceed limit)")
            knives_count = int(input('How many knives would you like to purchase: '))
        print(f"Ladels are ${LADELS:.2f}. We have 5 ladels left.")
        ladels_count = int(input("Enter the number of ladels you would like: "))
        while ladels_count <= 0 or ladels_count > 5:
            print("Error: Please enter an appropriate answer (Do not enter zero, a negative number, or exceed limit)")
            ladels_count = int(input('How many ladels would you like to purchase? '))
        print(f"Sauce pans are ${SAUCE_PANS:.2f}. We have 7 sauce pans left.")
        sauce_pans_count = int(input("Enter the number of sauce pans you would like: "))
        while sauce_pans_count <= 0 or sauce_pans_count > 7:
            print("Error: Please enter an appropriate answer (Do not enter zero, a negative number, or exceed limit)")
            sauce_pans_count = int(input('How many sauce pans would you like to purchase? '))
        knives_price = knives_total(knives_count)
        ladels_price = ladels_total(ladels_count)
        sauce_pans_price = sauce_pans_total(sauce_pans_count)
        total = calculate_total(knives_price, ladels_price, sauce_pans_price)
        tax = calculate_tax(total)
        amount_due = calculate_amount_due(total, tax)
        order_number = random.randint(10000, 100000)
        current_date_time = datetime.datetime.now()
        formatted_date_time = datetime.datetime.strftime(current_date_time, "%m/%d/%Y  %H:%M:%S")
        print_receipt(knives_count, ladels_count, sauce_pans_count, knives_price, ladels_price, sauce_pans_price, 
                      total, tax, amount_due, order_number, formatted_date_time)
        print(f"Receipt printed to {order_number}_Receipt.txt.")
        proceed = input("Would you like to make another purchase? (Enter y for yes): ")
    print("Thank you shopping at Jarod's Kitchenware Shop!")

def knives_total(knives_count):
    return knives_count * KNIVES

def ladels_total(ladels_count):
    return ladels_count * LADELS

def sauce_pans_total(sauce_pans_count):
    return sauce_pans_count * SAUCE_PANS

def calculate_total(knives_price, ladels_price, sauce_pans_price):
    return knives_price + ladels_price + sauce_pans_price

def calculate_tax(total):
    return total * TAX_RATE

def calculate_amount_due(total, tax):
    return total + tax

def print_receipt(knives_count, ladels_count, sauce_pans_count, knives_price, ladels_price, sauce_pans_price, 
                  total, tax, amount_due, order_number, formatted_date_time):
    with open(f"{order_number}_Receipt.txt", 'w') as receipt_file:
        receipt_file.write(f"Jarod's Kitchenware Shop Receipt\n")
        receipt_file.write(f"{'1115 Jaeger Drive':^32}\n")
        receipt_file.write(f"{'Paradis, WA':^32}\n")
        receipt_file.write(f"{'PHONE: 1(120)-007-1989':^32}\n")
        receipt_file.write(f"{formatted_date_time:^32}\n")
        receipt_file.write(f"{'ORDER #':>16}{order_number:<16}\n")
        receipt_file.write("--------------------------------\n")
        receipt_file.write(f"Knives {knives_count:>25}\n")
        receipt_file.write(f"{knives_price:>32.2f}\n")
        receipt_file.write(f"Ladels {ladels_count:>25}\n")
        receipt_file.write(f"{ladels_price:>32.2f}\n")
        receipt_file.write(f"Sauce Pans {sauce_pans_count:>21}\n")
        receipt_file.write(f"{sauce_pans_price:>32.2f}\n")
        receipt_file.write(f"Total {total:>26.2f}\n")
        receipt_file.write(f"Tax {tax:>28.2f}\n")
        receipt_file.write(f"Amount Due {amount_due:>21.2f}\n")
        receipt_file.write("--------------------------------\n")
        receipt_file.write(f"{'**** Thanks for your visit! ****':^32}")

kitchenware_order()