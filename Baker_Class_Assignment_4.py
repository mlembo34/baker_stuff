num = int(input("How many numbers do you need to check? "))
div_three = 0
not_div_three = 0

for i in range(num):
    check = int(input("Enter number: "))
    if check % 3 == 0:
        div_three += 1
        print(str(check) + " is divisible by 3.")
    else:
        not_div_three += 1
        print(str(check) + " is not divisible by 3.")
        
print("You entered " + str(div_three) + " number(s) that are divisible by 3.")
print("You entered " + str(not_div_three) + " number(s) that are not divisible by 3.")