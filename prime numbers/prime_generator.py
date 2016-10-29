def is_prime(num):
    if num > 1:
        for x in range(2,num):
            if num%x == 0: #check if modulus of num with x is zero
                return False    #if its zero means its divisible by the x so not prime
        else:
            return True #if non returns zero its prime
    else:
        return False #if num is one its not prime
def generate_primenumbers(n):
    print "Prime numbers in n"

    for number in range(2, n + 1): #numbers from 2 to n+1 checking for prime
        if is_prime(number):
            print number

print generate_primenumbers(20)
