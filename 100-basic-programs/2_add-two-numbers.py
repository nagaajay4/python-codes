# Read two values
num1=input("Enter the number: ")
num2=input("Enter the another number: ")

#compute the sum
sum=float(num1)+float(num2)

#print the values
print('the sum of {0} and {1} is {2}'.format(num1,num2,sum))


# single line solution
print('the sum of two numbers is: %.1f'%(float(input("Enter the number: "))+float(input("Enter the another number: "))))