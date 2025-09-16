print("Enter the first number:")
first_num = int(input())
print("Enter the second number:")
sec_num = int(input())
sum = first_num*sec_num
print(first_num,"x",sec_num,"=",sum)
if sum > 0:
    print("The result is positive.")
elif sum == 0:
    print("The result is positive and negative.")
else:
    print("The result is negative")