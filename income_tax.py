

"""
Probelm: Generating Random Characters

Now let us consider how to generate a random lowercase letter. The ASCII
code for lowercase letters are consecutive integers starting from the ASCII
code for 'a', then for 'b', 'c', ..., and 'z'. The ASCII code for 'a' is
ord('a')

❑ So, a random integer between ord('a') and ord('z') is

random.randint(ord('a'), ord('z'))
❑ And, a random lowercase letter is

chr(random.randint(ord('a'), ord('z')))

❑ To generalize the foregoing discussion, a random character between any two
characters ch1 and ch2 with ch1 < ch2 can be generated as follows:
chr(random.randint(ord(ch1), ord(ch2)))

"""
def generating_random_character():
    pass

## Simple Math Tool
"""
Write a program for a first grader to practice additions.
The program should randomly generate two single-digit
integers number1 and number2 and display a question
such as “What is 7 + 9?” to the student. After the
student types the answer, the program should displays
a message to indicate whether the answer is true or
false.

"""
def math_tool():

Print("what is %y + 9%")


##Taxes

status = 0
income = 1000

if (status == 0) and (income > 0 and income <= 8350):
    print("this is right")

if __name__ == '__main__':
