Main_Table = []
for i in range(10):
    if i%2 == 0:
        row1 = list(range(i*10+1,i*10+11))
    else :
        row1 = list(range(i*10+10,i*10,-1))
    Main_Table.append(row1)

ends_and_firsts = []
for i in Main_Table:
    ends_and_firsts.append(i[0])
    ends_and_firsts.append(i[-1])



nishs = [(99,6),(88,67),(71,29),(55,13),(24,1)]

nardeboons = [(8,31),(15,97),(42,81),(66,87)]

def is_nish(current):
    temp = False
    val = 0
    for m in nishs:
        a,b =m[0] , m[1]
        if a == current:
            temp = True
            val = b
            break
    return temp,val

def is_nardeboon(current):
    temp = False
    val = 0
    for m in nardeboons:
        a,b =m[0] , m[1]
        if a == current:
            temp = True
            val = b
            break
    return temp,val

def return_pos(current):
    x,y,counter = 0,0,0
    for i in Main_Table:
        counter+=1
        if current in i :
            y = counter
            x = i.index(current)+1  
    return x,y

def return_x_y(home):
    last_x , last_y = return_pos(home)
    x = (last_x-1) * 60
    y = (10-(last_y-1)) * 60 
    return x , y

# print(Main_Table)