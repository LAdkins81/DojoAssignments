def draw_stars(x):
    starStr = ""
    for val in x:
        count = 0
        while count < val:
            starStr = starStr + "*"
            count += 1
        print starStr
        starStr = ""
    return starStr

new = draw_stars([1, 9, 33, 4])
print new
