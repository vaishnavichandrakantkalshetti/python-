name=input("Enter your name")
marks=[]

n=int(input("enter how many marks you want to enter"))

for i in range(0,n):
    marks.append(int(input()))
    
print("marks are",marks)
total=sum(marks)
print("total of marks is:",total)

avg=total/n
print(avg)
