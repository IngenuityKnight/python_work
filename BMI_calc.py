"""Body Mass Index"""


def bmi():
    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height in Meters:"))

    bmi_total = weight / (height ** 2)
  ##  print("Your BMI is" bmi_total)
    if bmi_total <= 18.5:
        print("You are Underweight")
    elif bmi_total < 25:
        print("You are Normal")
    elif bmi_total <= 30:
        print("You are Overweight")
    elif bmi_total >= 30:
        print("You are Obese")

bmi()