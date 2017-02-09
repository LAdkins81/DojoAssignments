def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [1,2,5]
#b = multiply(a, 1)
#print b

def layered_multiples(func):
    totalArray = []
    #print newArray
    for val in func:
        count = 0
        newArray = []
        totalArray.append(newArray)
        while count < val:
            newArray += [1]
            count += 1
    return totalArray

new = layered_multiples(multiply(a, 5))
print new
