# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0: #replace or with and
            print("FizzBuzz")
        elif number % 3 == 0: #replace if with elif
            print("Fizz")
        elif number % 5 == 0: #replace if with elif
            print("Buzz")
        else:
            print(number) #remove square brackerts from number

fizz_buzz(15)