""" 
A useful technique for catching typing errors is to use a check digit. For example, suppose that a school assigns a six-digit number to each student. A seventh digit can be determined from the other digits with the use of the following formula:
    7t​h​digit=(1*(1s​t​digit)+2*(2n​d​digit)+...+6*(6t​h​digit))mod10
When a user types in a student number, the user types in all seven digits, If the number is typed incorrectly, the check digit will fail in 90% of the cases. Write an interactive program that prompts for a six-digit student number and reports the check digit for that number, using the preceding formula.

"""

def problem1(num):
    strNum = str(num)   
    digit8 = 0
    for i in range(1,7):
        digit8 +=i*(int(strNum[i-1]))

    return strNum+str(digit8%10)

print(problem1(123456)) 
print(problem1(724578))

