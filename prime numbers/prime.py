#A function to generate prime numbers from 0 to n with asymptotic analysis

def prime_numbers(): #defining function

    n = input("Enter n to generate Prime Numbers to: ") #Taking input for n to generate prime numbers to
    for num in range(0, n): #get numbers from zero to n
        if num > 1:
            for factor in range(2, num): #geting i to divide num with
                if (num % factor) == 0: #checks if number is prime by dividing with the other numbers
                    break
            else:
                print(num) #if above fails number is prime print it out


prime_numbers() #calling function