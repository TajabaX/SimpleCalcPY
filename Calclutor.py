def sum(num1, num2):
    result = num1 + num2
    print(result)
def min(num1, num2):
  result2 = num1 - num2
  print(result2)

def mul(num1, num2):
    result3 = num1 * num2
    print(result3)
def div(num1, num2):
  result4 = num1 / num2
  print(result4)

def rem(num1, num2):
  result5 = num1 % num2
  print(result5)

num1 = float(input("Enter a number:"))
num2 = float(input("Enter a second number:"))
operator = input("Enter Operator (+,-,*,/,%):")

if (operator == "+"):
    sum(num1,num2)

elif (operator == "-"):
    min(num1,num2)

elif (operator == "*"):
    mul(num1,num2)

elif (operator == "/"):
    div(num1,num2)

elif (operator == "%"):
    rem(num1,num2)

