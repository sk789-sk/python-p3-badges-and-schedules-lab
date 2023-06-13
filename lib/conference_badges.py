def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    out = []
    for val in names:
        out.append(badge_maker(val))
    return out

def assign_rooms(names):
    i = 0
    out = []
    while i < len(names):
        out.append(f"Hello, {names[i]}! You'll be assigned to room {i+1}!")
        i+=1
    return out

def printer(names):
    array = []
    for val in names:
        # print(val)
        array.append(badge_maker(val))

    for val in assign_rooms(names):
        array.append(val)
    for val in array:
        print(val)    
    return None

printer(["Arel", "Carol"])