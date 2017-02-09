#for loop that prints all odd number from 1 to 1000
for count in range(0, 1000):
    if not count % 2:
        continue
    print count
#for loop that prints the multiples of 5 from 5 to 1,000,000; change to 1000000 before submitting
for count in range(5, 1000000):
    if count % 5 != 0:
        continue
    print count
#print the sum of this list
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b
#find the average of the list
avg = b / len(a)
print avg
