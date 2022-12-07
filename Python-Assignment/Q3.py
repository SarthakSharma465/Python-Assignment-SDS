list = [15,47,68,89,35,13]
for i in range (0,6):
 for j in range (i+1,6):
  if (list[i]>list[j]):
   list[i], list[j] = list[j], list[i]
  

print(list) 
 
