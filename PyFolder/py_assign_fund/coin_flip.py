import random
def coin_flip():
    heads = 1.0
    tails = 0.0
    total_cnt = 0
    heads_cnt = 0
    tails_cnt = 0
    for count in range(1, 5001):
        total_cnt = total_cnt+1
        random_num = round(random.random())
        if random_num == 1.0:
            heads_cnt = heads_cnt+1
            print "Attempt #"+str(total_cnt)+": It's a head! I got("+str(heads_cnt)+")head(s) so far and ("+str(tails_cnt)+") tails so far"
        elif random_num == 0.0:
            tails_cnt = tails_cnt+1
            print "Attempt #"+str(total_cnt)+": It's a tail! I got("+str(heads_cnt)+")head(s) so far and ("+str(tails_cnt)+") tails so far"
    print "Ending the program, thank you!"
    return coin_flip
now = coin_flip()
print now
