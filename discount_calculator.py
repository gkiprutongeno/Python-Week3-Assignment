
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if the discount is at least 20%
        discount_rate = discount_percent / 100  # Convert the discount percent to a decimal for calculation
        discount_amount = price * discount_rate  # Calculate how much money is taken off
        final_price = price - discount_amount  # Subtract the discount from the original price
        return final_price  # return the discounted price
    else:
        return price  # If discount is less than 20%, return the original price

# input() returns text, so we convert to float for math
price_input = float(input("Enter the original price: "))
discount_input = float(input("Enter the discount percentage: "))

#Basic validation to keep values sensible
if price_input < 0:
    print("Error: Price cannot be negative.")
elif discount_input < 0 or discount_input > 100:
    print("Error: Discount percent must be between 0 and 100.")
else:
    # Compute the final price using our function
    final_price = calculate_discount(price_input, discount_input)

    # Decide what to tell the user based on the discount rule
    if discount_input >= 20:
        print(f"Discount applied: {discount_input}%")
        # :.2f formats the number to 2 decimal places (like money)
        print(f"Final price: {final_price:.2f}")
    else:
        print("No discount applied (less than 20%).")
        print(f"Final price (original price): {final_price:.2f}")
