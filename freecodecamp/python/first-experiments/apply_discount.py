# | Apply-Discount function freecodecamp python exercise |
#
# In this lab you will write a function that calculates the final price of an item after applying a percentage discount.
# Instructions:
# 1. You should define a function named apply_discount.
# 2. The apply_discount function should take exactly two parameters: price and discount.
# 3. If price is not a number (int or float), the function should return the string The price should be a number.
# 4. If discount is not a number (int or float), the function should return the string The discount should be a number.
# 5. If price is less than or equal to 0, the function should return the string The price should be greater than 0.
# 6. If discount is less than 0 or greater than 100, the function should return the string The discount should be between 0 and 100.
# 7. If both inputs are valid, the function should calculate the discount as a percentage of the price.
# 8. The function should return the final price after applying the discount.
#
# In this exercise, I was not instructed to finish the program by adding output, and real variables for the (price, discount) paramaters. So I
# finished it myself. This exercise helped refresh me on the isinstance built-in function, as well as practice mathematic operations.
#
# Here's how it works:
#
# Formula: Price minus (Price × Discount ÷ 100)
# Example: 200 - (200 x 20 ÷ 100) | 200 - ( 4000 ÷ 100) | 200 - 40 | 160

price = 200
discount = 20

def apply_discount(price, discount):

    if not isinstance(price, (int, float)):
        return "The price should be a number"

    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    if price <= 0:
        return "The price should be greater than 0"

    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    return price - (price * discount /100)

grand_total = apply_discount(price, discount)
print('-----------------------')
print('Discounted Total:', grand_total)
print('-----------------------')


# Output:

# -----------------------
# Discounted Total: 160.0
# -----------------------
