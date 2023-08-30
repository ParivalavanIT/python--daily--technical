def fizzbuzz(start,end):
    if start % 3 == 0 and start % 5 == 0 :
        print ("Fizz Buzz")
    elif start % 3 == 0 :
        print ("Fizz")
    elif start % 5 == 0 :
        print ("Buzz")   
    else:
        print(start)
     
    if start != end :
        return fizzbuzz(start+1,end)
    else:
        pass
    
    
fizzbuzz(1,100)