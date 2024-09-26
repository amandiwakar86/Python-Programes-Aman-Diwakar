# Electricity Bill Calculator
# Take the Units by the User
units = int(input("Enter the Units : "))
bill_amount = 0
# Perform the task
if units <=150:
    bill_amount = units*5.50
elif units >= 151 and units <=300:
    bill_amount = (150*5.50)+(units-150)*6
elif units >= 301 and units <= 500:
    bill_amount = (150*5.50)+(300-151)*6 + (units-300)*6.50
elif units >= 501:
    bill_amount = (150*5.50)+(300-151)*6 + (500-300)*6.50 + (units-500)*7
# 15% Tax Charge
tax = bill_amount*15/100
payble_amount = bill_amount + tax
print("Total Payble amout is: ", payble_amount)



