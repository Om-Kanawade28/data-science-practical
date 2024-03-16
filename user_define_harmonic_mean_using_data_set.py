data_set = [2,3,4,5,6]
def harmonicMean(data_set):
    sum = 0
    for i in data_set:
        sum += 1/i
    return len(data_set)/sum
print("harmonic mean=",harmonicMean(data_set))
