length=int(input("Enter the length of the array"))
arry=[]
if(length<3):
  print("Error in determination of the range")
else:
  for i in range(0,length):
    m=int(input(f"enter the elements in pos{i}"))
    arry.append(m)
diff=max(arry)-min(arry)
print(diff)
