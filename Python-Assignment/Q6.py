list_even = []
list_odd = []

n = int(input("Length of the list "))
for i in range(0,n):
    even = int(input("Enter elements "))
    list_even.append(even)


print(list_even)
    
k = int(input("Length of the list "))
for j in range (0,k):
    odd = int(input("Enter elements "))
    list_odd.append(odd)
    
print(list_odd)


list_new = []


for i in range (0,n):
 if ((list_even[i] % 2) == 0):
     list_new.append(list_even[i])


for j in range (0,k):
    if ((list_odd[j] % 2) == 1):
        list_new.append(list_odd[j])


print(list_new)


    
