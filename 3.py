list=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    val=int(input("Enter the number: "))
    list.append(val)
largest=list[0]
for n in list:
    if n>largest:
        largest=n   
print("The largest number is:",largest)





