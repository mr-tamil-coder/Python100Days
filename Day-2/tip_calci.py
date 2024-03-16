print("Welcome to the tip calculator ")
total_bill=float(input("What was the total bill"))
tip=int(input("how much tip would u like to give ? int value"))
split_bill=int(input("how many people to split"))
to_pay=(total_bill+total_bill*tip/100)/split_bill
result=round(to_pay,2)
print(f"Each person should pay: {result}")