#find the median number
 
a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
c = int(input("Please enter a third number: "))
 
if a > b:
   if a < c:
       print("The median is: ", a)
   elif b > c:
       print("The median is: ", b)
   else:
       print("The median is: ", c)
else:
   if a > c:
       print("The median is: ", a)
   elif b < c:
       print("The median is: ", b)
   else:
       print("The median is: ", c)


https://docs.google.com/document/d/1DuFZt3EDLtECdyYCC3vqhaq4IKa39YiIr1OaToX1Yqg/edit
 
 
