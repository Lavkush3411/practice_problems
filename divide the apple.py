def apple_dvider():
    try:
        for i in range(mn,mx+1):
            if n%i==0:
                print(f"{n} apples can be give to {i} students perfectly")
            else:
                print(f"{n} apples can't dvided properly into {i} students each gets{n//i} apples & apple will be remain = {n%i}")
    except:
        print("Something went wrong")
mn=0
mx=1
n=0
try:
    n=int(input("enter the total number of apples = "))
    mn=int(input("Enter minimum number of students = "))
    mx=int(input("Enter maximum number of students = "))
except:
    print("invalid input")
if mn==mx:
    print("your range of students is equal")
    if n%mn==0:
        print(f"{n} is divided by {mn}")
    else:
        print(f"{n} is not divisible by {mn}")
else:
    apple_dvider()
input()