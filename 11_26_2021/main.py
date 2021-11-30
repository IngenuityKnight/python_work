# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
''

# Press the green button in the gutter to run the script.
def test():
    for i in range(10):
        print("Hello Cameron", i)

def compute_area():
    radius=20.0
    area=radius * radius * 3.14159
    print("The area for the circle of radius {} is {}".format(radius,area))

def convert_sec(time_in_sec):
    min = int((time_in_sec / 60))
    sec = time_in_sec %60
    time = "{} minutes and seconds {}".format(min,sec)
    return time

if __name__ == '__main__':
    print ("Hello World")
    my_value=input("enter your age: ")
    print(type(10))

    print(type(my_value))
    print("My age is {}".format(my_value))
    ##compute_area()
    test()
    time_converted = convert_sec(150)
    print(time_converted)