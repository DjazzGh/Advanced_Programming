num = float(input("Number: "))

if(num%3==0 and num%5==0):
    print("FizzBuzz")
elif(num%5==0):
    print("Buzz")
elif(num%3==0 ):
    print("Fizz")
