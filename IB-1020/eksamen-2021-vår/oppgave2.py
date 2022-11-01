def average(list):
    sum = 0
    for number in list:
        sum += number
    return sum / len(list)

def variance(list):
    sum = 0
    avg = average(list)
    for number in list:
        sum += (number - avg)**2
    return sum / len(list)

x = [9, 17, 5, -3, 2]
print(variance(x))