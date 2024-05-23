def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        price = price * discount_percent/100
        return price
    else:
        return price
    
print(f"The final price is {calculate_discount(int(input("Enter the original price")), int(input("discount")))}")



