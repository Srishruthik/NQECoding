import math # or instead of math.sqrt multiply
"""

The theory of relativity holds that as an object moves, it gets smaller. The new length of the object can be determined from the formula:
New length = Original Length * sqrt( 1 – B2​ ​ )
where B2​ ​ is the percentage of the speed of light at which the object is moving, entered in decimal form. Given the length of an object, print its new length for speeds ranging from 0 to 99.99 percent of the speed of light. Print the output in a table.

"""
def relativeLen():
    lightPercent = [
         0,
        25,
        50,
        75,
        90,
        95,      
        99,
        99.99,
    ]
    SPEED = 300000000

    speedms = [(int((SPEED*light)/100)) for light in lightPercent]

    newlen = [10*(math.sqrt(1-((lendec/100)**2))) for lendec in lightPercent]

    #formating the output
    print("Percent of light Speed(m/s) \tLength")
    print("---- \t\t ---- \t\t --")
    for light,speed,len in zip(lightPercent,speedms,newlen):
        if len == 10:
            print(str(light)+"%\t\t"+str(speed)+"\t\t"+str(len))
        else:
            print(str(light)+"%\t\t"+str(speed)+"\t"+str(len))
    

(relativeLen())
