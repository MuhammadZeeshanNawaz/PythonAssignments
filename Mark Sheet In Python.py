#zeeshan_nawaz
print ("Enter Your Marks in Physics")
physics = int (input())
print ("Enter Your Marks in Maths")
maths = int (input())
print ("Enter Your Marks in Computer")
computer = int (input())


result = physics + maths + computer
result_1 = (result / 300) * 100
if physics >= 0 and physics < 101 and maths >= 0 and maths < 101 and computer >= 0 and computer < 101:

    if result_1 < 40 or physics < 40 or maths < 40 or computer < 40 :
        print("You Secure grade F")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")
        
    elif result_1 > 79 and result_1 < 101:
        print("You Secure grade A+")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")
    
    elif result_1 > 69 and result_1 < 80:
        print("You Secure grade A")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")
    
    elif result_1 > 59 and result_1 < 70:
        print("You Secure grade B")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")
    
    elif result_1 > 49 and result_1 < 60:
        print("You Secure grade C")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")
    
    elif result_1 > 39 and result_1 < 50:
        print("You Secure grade D")
        print("Your Total Marks is: ",result)
        print("Your Percentage is: ",round (result_1,2),"%")


        
else:
    print("Please make sure your marks are valid try again")