"""
Create a function named calculate_discount(price, discount_percent)
 that calculates the final price after applying a discount. 
 The function should take the original price (price) and 
 the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, 
return the original price.
"""
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:

        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    
# Using the calculate_discount function, 
# prompt the user to enter the original price of an item and the discount percentage. 
# Print the final price after applying the discount, 
# or if no discount was applied, print the original price.

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numerical values.")


    