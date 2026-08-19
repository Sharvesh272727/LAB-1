#For loop

#Question 1:
print numbers from 1 to 10

for i in range(1,11):
    print(i)
 
#Question 2:
print numbers 10 to 1

for i in range(10,0,-1):
    print(i)

#Question 3:
print all even numbers from 1 to 20

for i in range(1,21):
 if i%2==0:
     print("Even number:",i)

#Question 4:
print all odd numbers from 1 to 20

for i in range(1,21):
 if i%2!=0:
     print("odd number:",i)

#Question 5:
print multiplication of number

for i in range(1,11):
    print('5','*',i,'=',5*i)

#Question 6:
sum of number from 1 to 100

a=0
for i in range (1,101):
 a=a+i
print(a)


#Question 7:
sum of even numbers from 1 to 50

a=0
for i in range(1,51):
    if i%2==0:
        a=a+i
print(a)


#Question 8:
print each character of string 'PYTHON'

for i in "PYTHON":
    print(i)

#Question 9:
count the number of character in string without
using len()

count=0
for i in "PYTHON":
    count+=1
print(count)




#Question 10:
Square of numbers from 1 to 10


for i in range(1,11):
    print(i**2)
    















