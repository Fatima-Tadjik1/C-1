def fizzbuzz(range_a, range_b):
    
    for i in range(range_a, range_b):
        if i % 3== 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

            
fizzbuzz(1,101)
