try:
   user_input = int(input("enter the number:"))
   if user_input==1 and user_input==0:
     print("factorial is 1")
     i=1
     fact=1

   while i<=user_input:
       fact=fact*i
       i+=1
   print(fact)
except:
   if user_input<0:
      print("Negative number not have a factorial")
   
  