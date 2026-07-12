nums=[2,7,4,1,3,6]
count=0
leng=len(nums)
for i in range(leng):
  for j in range(leng-1):
    if((nums[j]+nums[i])==10):
      count+=1
print(count)
