
def comma(List):
    Length = len(List) # number of strings within the list
    
    expression = List[1:Length-1]
    print(expression)  
    #expression = expression + " and " + List[Length]
    print(str(expression).strip('[]') + " and '" + str(List[-1]) + "'")
    
  #  for count in range(1, Length+1):
   #     print (count, Length)
    #    if (count == 1):
     #       expression = List[0]
      #  elif (count > 1):
       #     expression = expression + ","+ List[count-1]
        #    if count == Length:
         #       print(expression)
          #      return expression

mylist = input("Enter a list of strings, SEPERATED by WHITE SPACSPACE: ")
mylist = mylist.split()
comma(mylist)