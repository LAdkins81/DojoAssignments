x = [16,'Jill',5,'Laura',22,'Terry Adkins']

def draw_stars_2(list1):
    for i in list1:
        if type(i) == int:
            print "*" * i
        elif type(i) == str:
            print i[0].lower()*len(i)
    #return "sucess"
draw_stars_2(x)
