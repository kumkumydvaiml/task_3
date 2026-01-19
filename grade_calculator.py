print("-------Grade Calculation.----------")
# Here I am taking input from the user 
marks1=float(input("Enter subject 1 marks :"))
marks2=float(input("Enter subject 2 marks :"))
marks3=float(input("Enter subject 3 marks :"))
marks4=float(input("Enter subject 4 marks :"))
marks5=float(input("Enter subject 5 marks :"))

total=marks1+marks2+marks3+marks4+marks5
percent=total//5

if percent>=90 or percent<=100:
    print(f"You got {percent} with A+,Excellent")
elif percent>=80 or percent<=89:
    print(f"You got {percent} with A,Very Good")
elif percent>=70 or percent<=79:
    print(f"You got {percent} with B+,Good")
elif percent>=60 or percent<=69:
    print(f"You got {percent} with B, Above Average")
elif percent>=50 or percent<=59:
    print(f"You got {percent} with C, Average")
elif percent>=40 or percent<=49:
    print(f"You got {percent} with D,Pass")
elif percent<40:
    print("You got with F, Fail")
else:
    print("Invalid Marks...")

print("Thanks For Visting Here :) ")
