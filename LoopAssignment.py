#9.	Make a program that asks ten numbers and in the end prints out two biggest numbers.
user_input = input("Enter the numbers separated by a space ").split()

int_list = list(map(int, user_input))

print ("Max number:",max(int_list), "\nMin number:",min(int_list))

#1.	Make a program that prints all positive numbers that are odd and smaller than 100 starting from 1. (1 3 5 7 9 11…)
start, end = 2, 99
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end = " ")
