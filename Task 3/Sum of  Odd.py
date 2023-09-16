'''
Question:-You are given a list. Return the sum of odd elements from the given list. 
The input and output portions will be handled automatically. 
You need to write a function with the recommended method signature.

Constraints:-
The list will have 1-100 elements.
Each element will be an integer X where -100<=X<=100. 
'''
def Odd_Summation():
    sum = 0
    to_calc = eval(input("Enter: "))
    for num in to_calc:
        if num%2 != 0:
            sum += num
        else:
            pass
    print(sum)

Odd_Summation()
