# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

#n = int(input("Enter number "))
# pass range of numbers to sum() function
#x = sum(range(1, n + 1))
#print('Sum is:', x)

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
