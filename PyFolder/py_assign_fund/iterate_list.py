def friend(x):
    newfriend = []
    for person in x:
        if len(person) == 4:
            newfriend.append(person)
            return newfriend


result = friend(["Bob", "Jim", "Mark", "Jill", "Riley"])
print result
