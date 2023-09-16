def Odd_Summation():
    sum = 0
    to_cal = eval(input("Enter: "))
    for num in to_cal:
        if num%2 != 0:
            sum += num
        else:
            pass
    print(sum)

Odd_Summation()