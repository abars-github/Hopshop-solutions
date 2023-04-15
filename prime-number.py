# Determine if a number is Prime:

num = int(input("Enter a positive number:"))
if num > 1:
    for x in range (2,num):
        if (num%x)==0:
            print("False")
            break
    else:
        print("True")
else:
    print("False")
