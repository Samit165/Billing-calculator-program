item_name = input("Enter the item Name:")
if not item_name:
    print("Please fill")
    exit()

while True:
    try:
     qty = int(input("Enter Quantity: "))
     if qty<=0:
         print("Invalid")
     else:
         break
    except ValueError:
        print("Invalid input")
        
while True:
    try:
        unit_price = float(input("Enter Unit Price: "))
        if unit_price <= 0:
         print("Invalid")
        else:
            break
    except ValueError:
     print("Invalid input")
    
while True:
        try:
            tax_rate = float(input("Enter Tax Rate: "))
            if 0<= tax_rate <=100:
                break
            else:
                print("Invalid")
        except ValueError:
            print("Invalid Input")
            
            
sub_total =  qty * unit_price

discount = 0.0
if sub_total >1000:
    discount = sub_total * 0.05
    
discounted_sub_total = sub_total-discount
tax_amount = discounted_sub_total * (tax_rate/100)
final_total = discounted_sub_total+tax_amount
sub_total = round(sub_total,2)
discount =  round(discount,2)
tax_amount = round(tax_amount,2)
grand_total = round(final_total,2)

print("\n-------------------------------------------")
print(f"Item name      :{item_name}")
print(f"Quantity       :{qty}")
print(f"Unit Price     :{unit_price:.2f}")
print("-----------------------------------------------")
print(f"Original Subtotal:{sub_total:.2f} ")
print(f"Discount Amount  :{discount:.2f}")
print(f"Tax Amount       :{tax_amount:.2f}")
print("------------------------------------------------")
print(f"Grand total      :{grand_total:.2f}")
    
    
     