string = input("Enter a string: ")
l = len(string)
j = 0
i=0

while len(string)!=0:    
 ch = string[i]
 k=0
 print("{" + ch + ":",end ="")
 for j in range (i,len(string)):
     if (string[j] == ch):
      k+= 1
 print(k, end ="}")
 string = string.replace(ch, "")
 
 

#if(string[j] == string[i] and j>i):
   # string.replace(string[j], "")


##
##string = input("Enter a string: ")
##l = len(string)
##j = 0
##for i in range (0,l):    
## ch = string[i]
## k=0
## print("{" + ch + ":",end ="")
## for j in range (i,l):
##     if (string[j] == ch):
##      k+= 1
## print(k, end ="}")
## string = string.replace(ch, "")
##
##
##        
##        
##
