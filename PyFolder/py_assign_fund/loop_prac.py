for count in range(0, 5):
    print "looping - ", count
count = 0
while count < 5:
    print "looping - ", count
    count += 1
for val in "string":
    if val == "i":
        continue #break is another option; will only print UP TO that value
    print(val)
for count in range(1, 20):
    if count % 2 == 0:
        print "Number is " + str(count) + ". This is an even number."
    elif count % 2 != 0:
        print "Number is " + str(count) + ". This is an odd number."
