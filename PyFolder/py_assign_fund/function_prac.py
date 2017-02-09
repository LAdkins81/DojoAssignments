#prints odd and even numbers in range; change range to 2001 before submitting
def even_odd():
    for count in range(1, 21):
        if count % 2 == 0:
            print "Number is " + str(count) + ". This is an even number."
        elif count % 2 != 0:
            print "Number is " + str(count) + ". This is an odd number."
    return
result=even_odd()
print result
#multiplies values in a list times a given number
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [1, 9, 2]
# b = multiply(a, 5)
# print b
#hacker challenge - be sure to comment out var b and print b before running layered_multiples to work properly
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

new = layered_multiples(multiply(a, 4))
print new
