# 1
def countdown(num):
    output =[]
    for i in range(num, -1 , -1):
        output.append(i)
    return output
print(countdown(10))

# 2
def num(list):   
    print(list[0])
    return(list[1])
print(num([1,2]))

# 3
def firt_plus_length(list):
    return list[0] + len(list)
print(firt_plus_length([1,2,3,4,5,6,7,8,9,10]))

# 4
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output =[]
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output
    
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5
def length_and_value(size,value):
    output =[]
    for i in range(0,size):
        output.append(value)
    return output
print(length_and_value(4,7))
print(length_and_value(6,2))       

        

    



    
    