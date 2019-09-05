total_bill_amount = float(input('Total bill amount? $'))
print('Level of service?')
service = input('Please choose good, fair, or poor,')
if service == "good":
    tip = (total_bill_amount * 0.20)
    total = (total_bill_amount + tip)

if service == "fair":
    tip = (total_bill_amount * 0.15)
    total = (total_bill_amount + tip)

if service == "poor":
    tip = (total_bill_amount * 0.10)
    total = (total_bill_amount + tip)

print('The tip is ', tip)
print('The total is ', total)
