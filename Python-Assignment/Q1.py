string = input("Enter string ")
a = len(string)
c= (a+1)/2
    
# odd
if (a%2) != 0:
   
  for n in range (0,int(c)):
    i=2*n
  print(string[i])
 
else:

 for n in range (0,a//2):
    i=2*n
    print(string[i])
    


 
