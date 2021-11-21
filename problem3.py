"""
The Lucas numbers are a series of numbers closely related to the Fibonacci numbers. The nth Lucas number, written L​n,​ isdeterminedasfollows: 
"""
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1

    elif n> 1:
        return lucas(n-1)+lucas(n-2)

def output():
    for i in range(0,31):
        print(lucas(i))

output()
