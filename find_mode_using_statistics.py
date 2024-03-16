#find range [4,10,29,33,42,67]
numbers = [4,10,29,33,42,67]
def  range(no):
    min_no = min(no)
    max_no = max(no)
    range_n = max_no - min_no
    print("range=",range_n)

    
range(numbers)
#range= 63
range([4,10,29,33,42,-67])
#range= 109