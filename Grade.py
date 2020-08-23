
#print the grade obtained by a student

#Algorithm
# step-1:START

# step-2:Initialize 4 floating inputs for the 
various 4 subjected like  Accounts,economics,
commerce,stock marketing

# step-3:Then evaluate the grade based upon 
  the average of four subjects of marks

# step-4:If the value of the grade is more than
40, it will print the grade A,B,C.otherwise 
the value of grade is less than 40 it will
 print the grade F.

# step-5:END

#Programmer Code
w=float(input("enter marks of Accounts"))
x=float(input("enter marks of economics"))
y=float(input("enter marks of commerce"))
z=float(input("enter marks of stock marketing"))

a=(w+x+y+z)/4

print('A grade',(a<=75))
print('B grade',(a>=65 and a<75))
print('C grade',(a>=40 and a<60))
print('F grade',(a<40))
