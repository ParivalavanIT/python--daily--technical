def fizzbuzz(i,j):
    if i%3==0 and i%5==0:
        print ("Fizz Buzz")
    elif i%3==0 :
        print ("Fizz")
    elif i%5==0 :
        print ("Buzz")   
    else:
        print(i)
     
    if i!=j :
        return fizzbuzz(i+1)
    else:
        return
    
    
fizzbuzz(1,100)