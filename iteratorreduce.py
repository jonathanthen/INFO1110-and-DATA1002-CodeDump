def average(numbers):
    if len(numbers) < 1:
        return 0
    avg = 0
    for num in numbers:
        avg += num
    avg = avg / len(numbers)
    return avg

#def average(numbers):
#    result = initial_value
#    for item in collection:
#        result = function(result, item)
#    return result