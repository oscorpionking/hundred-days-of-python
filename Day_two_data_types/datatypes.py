#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
num = input("enter number a:\n")

a = num[0]
b = num[1]
sara = int(a)+int(b)
print(sara)
print("The answer is: \n" + str(sara))

#different data types cannot be concatenated
#datatypes can be inter-converted using TYPE-CASTING.
#PERFORMING MATH operations uses the PEMDAS rule,
#going from left to right.

#EXCERCISE BMI CALCULATOR

#BMI = weight (kg)/height squared (meteres squared)
height = int(input("Please input your height in metres\n"))
weight = int(input("please input your weight in kg\n"))

bmi = int(weight/(height*height))
print(bmi)

#error invalid literal for int() with base 10 might come up if 
# a decimal number is used. to resolve first convert to float then integer

#so the above will be re-written as:
height = (float(input("Please input your height in metres\n")))
weight = (float(input("please input your weight in kg\n")))

bmi = int(weight/(height*height))
print(bmi)
#OR

w = float(weight)
h = (float(height)**2)
bmi = w/h
print(int(bmi))

#rounding decimal points
#using ROUND which takes the input to round and the number of figures to round to eg:
print(round(2.3344444,3))


# F-strings  - for strings formatting, adding data types  to strings
#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
age = input("How old are you today?\n")
week = 52*int(age)
left = (90*52)- week
print(f"You are currently {week} weeks old")
print(f"You have {left} weeks left until age 90.")