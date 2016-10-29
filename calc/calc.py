#NJIRU
#from __future__ import division

def try_1(num1,num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'substract':
        #if num1 < num2:
        #    return num2 - num1
        #else:
            return num1 - num2
    elif operation == 'multiply':
        return num1*num2
    elif operation == 'divide':
        return round(float(num1/num2),2)