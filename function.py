def calculate_discount(price, discount_percent):
    # Check if discount percent is 20 or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate and return the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user for the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Print the final price or the original price if no discount was applied
    print("The final price is:", final_price)

except ValueError:
    print("Please enter valid numeric values for the price and discount.")
