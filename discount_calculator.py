# Discount Calculation Challenge

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

if __name__ == "__main__":
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        final_price = calculate_discount(price, discount_percent)
        if final_price != price:
            print(f"Final price after {discount_percent}% discount: {final_price}")
        else:
            print(f"No discount applied. Original price: {price}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
