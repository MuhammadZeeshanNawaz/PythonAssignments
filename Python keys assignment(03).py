#Assignment no. 03
#question no 1:
val1= eval(input("Enter Your  Value 1:"))
val2= eval(input("Enter You Value 2:"))
operator = input("Enter Operator!! ")

if operator == "+":
 val = val1 + val2
 print(val,"Answer")
 
elif operator == "-":
 val = val1 - val2
 print(val,"Answer")
 
elif operator == "*":
 val = val1 * val2
 print(val,"Answer")
 
elif operator == "/":
 val = val1 / val2
 print(val,"Answer")
 
elif operator == "**":
 val = val1 ** val2
 print(val,"Answer")

else:
  print("plzz Enter Correct operator")
----------------------------------------
#question no 2:
l=['8','karachi','2','ALI','100','4']
for var in l:
    l =  [s for s in l if s.isdigit()]
    
print(l)
-----------------------------
#question no 3:
student = {"student_ID": "17b-066-CS ","Full Name": "Muhammad Zeeshan Nawaz", "department": "computer science" }

student["section"] = "A"
print(student)
----------------------------------
#question no 4:
val= {'val1':22,'val2':90,'val3':10}
print(sum(val.values()))
--------------------------------
#question no 5:
check_dup = [ 10, 30, 8, 7, 3, 10, 15, 12, 45, 5, 12, ]
dupItems = []
uniqItems = {}
for x in check_dup:
   if x not in uniqItems:
      uniqItems[x] = 1
   else:
      if uniqItems[x] == 1:
         dupItems.append(x)
      uniqItems[x] += 1
print(dupItems)
-------------------------------------
#question no 6:
student = {"student_ID": "17b-066-CS ","Full Name": "Muhammad Zeeshan Nawaz", "department": "computer science" }

if "student_ID" in student:
    print("Yes 'student' key exists in dict")
else:
    print("No 'student' key does not exists in dict")    


