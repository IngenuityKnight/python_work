def price_after_tax():
    prod_price = float(input("the price of the product: "))
    sale_tax_rate = 8.875
    return (prod_price * sale_tax_rate)/100
print("sale price after tax :{:.2f} ".format( price_after_tax()))
