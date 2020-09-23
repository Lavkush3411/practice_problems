"""practice problem number 1"""


current_age=input("Enter your born year or current age = ")
def year(c_a):
    print(f"for now you are of {2020-int(c_a)} years old")
    print(f'in {int(c_a)+100} your age will be of 100')
    n=input("Do u want to know in any year what will be your age y/n? = ")
    if n=="y":
        n2=input("enter any year = ")
        n3=int(n2)-int(c_a)
        if n3>0 and n3<150:
            print(f"your age in {n2} will be {n3}")
        else:
            print("you are too old or not born bro")
    else:
        print("Hmm okey then good bye")
def age(c_a):
    print(f"you were born in {2020-int(c_a)}")
    print(f'After {100-int(c_a)} your age will be of 100')
    n = input("Do u want to know in any year what will be your age y/n? = ")
    if n == "y":
        n2 = input("enter any year = ")
        n3 = int(n2) - 2020
        if n3 > 0 and n3 < 150:
            print(f"your age in {n2} will be {n3+c_a}")
        else:
            print("you are too old or not born bro")
    else:
        print("hmm okey then good bye")
if len(current_age)<=2:
    age(current_age)
elif len(current_age)==4:
    year(current_age)
else:
    print("hmm it seems you are too old")
input()