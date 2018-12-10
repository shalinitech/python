

total=0
count=0

while(True):
     inp=input("Enter a number:")
     if (inp=='done'):
      break
     try:
         val=float(inp)
     except:
         print("Invalid data")
         continue
     else:
      total=total+val
      count=count+1
      avg=total/count
print(total , count, avg)
