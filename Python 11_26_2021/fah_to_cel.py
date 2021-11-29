def fah_to_celc():
    degree_fah = int(input("Please enter degree: "))
    celc = (5/9)*(degree_fah - 32)
    return celc

print("the celsius {:.2f}".format((fah_to_celc())))
