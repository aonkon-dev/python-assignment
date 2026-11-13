customer_name = input("Enter customers name :")


products1 = input("Enter products 1 names:")
price1 = float(input("Enter products 1 price:"))

products2 = input("Enter products 2 names:")
price2 = float(input("Enter products 2 price:"))

products3 = input("Enter products 3 names:")
price3 = float(input("Enter products 3 price:"))

subtotal = price1 + price2 + price3

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05

else:
    discount_rate = 0.0


discount =   subtotal * discount_rate

finel_total = subtotal - discount



print(f"Customer Name:{customer_name}")

print(f"Product 1:{products1 }")
print(f"Price: {price1}")

print(f"Product 2:{products2 }")
print(f"Price: {price2}")

print(f"Product 3:{products3 }")
print(f"Price: {price3}")

print(f"Subtotal: {subtotal:g}")
print(f"Discount: {discount:g}")
print(f"Final Total: {finel_total:g}")