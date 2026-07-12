import random
import math

m2=[random.randint(1, 10) for i in range(25)]
length=len(m2)
mean = sum(m2)/length
m2.sort()
if length%2==1:  
    median=m2[length//2]
    print("The median is:",median)
else:  
    median1=m2[(length//2)-1]
    median2=m2[length//2]
    print("There are two medians:",median1,median2)
print("Mean:",mean)
print("Sorted List:",m2)

