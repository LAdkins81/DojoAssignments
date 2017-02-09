import random
def score():
    for count in range(1, 11):
        random_num = int(random.random()*40+61)
        if random_num > 89:
            print "Score: "+str(random_num)+"; Your grade is A"
        elif random_num < 89 and random_num > 79:
            print "Score: "+str(random_num)+"; Your grade is B"
        elif random_num < 79 and random_num > 69:
            print "Score: "+str(random_num)+"; Your grade is C"
        elif random_num < 69 and random_num > 59:
            print "Score: "+str(random_num)+"; Your grade is D"
    #for count in range(11,12):
    print "End of this program! Bye!"
    return score
now = score()
print now
