my_str = "If monkeys like bananas, then I must be a monkey"
print my_str.find("monkey")
print my_str.replace("monkey", "alligator")

x=[2,5,11,165,-4,22]
print max(x)
print min(x)

new_lst = ["hello", 42, 6, 99, "world"]
print new_lst[0] + new_lst[-1]
oth_list = [new_lst[0], new_lst[-1]]
print oth_list

y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
z = y[0:2]
y[0:2] = []
y = [z] + y
print y
