#Numerical Expressions

##Floating poing calculation

val1 = 1.395e5
val2 = 5.55e2
print(val1 + val2)

##Type conversion exercise 1

val1 = float(input("Enter val1: "))
val2 = float(input("Enter val2: "))
print(val1 + val2)

##Type conversion exercise 2

weight_in_grams = input("Enter weight in grams: ")
weight_in_kg = int(weight_in_grams) / 1000
weight_as_str = str(weight_in_kg) + 'kg'
print(weight_as_str)

#Operations in detail

##Happy Birthday Mr Frodo

days_lived = int(input("How many days have you lived? "))
years_old = days_lived//365
days_to_bday = 365 - days_lived % 365
message1 = "You are " + str(years_old) + " years young!"
message2 = "You have " + str(days_to_bday) + " days until you next get to boogie down."
print(message1)
print(message2)

## Mr Frodo goes to the bank

RATE = 0.045
amount = int(input("How much money would you like to invest, Mr Frodo? "))
time = int(input("How many days would you like to invest this for? "))
final_amount = amount*(1+RATE/12)**(time//31)
print("After that time you will have: $"+str(final_amount))