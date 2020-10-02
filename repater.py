import os
import time
def check_if_key_in_constants(key):
    sp_keys = {'space': Key.SPACE, 
     'backspace':Key.BACKSPACE,
     'enter' : Key.ENTER}
    if key in sp_keys.keys():
        return sp_keys.keys[key]
    else:
        return key


log_path = 'C:/Users/kir/Desktop/actions/log.txt'
dg = open(log_path,'r')
lines = dg.read().splitlines()
acts = {'Click' : click, 'DoubleClick' : doubleClick}
print(lines[0].split('|'))
for i in lines:
    lst = i.split('|')
    if lst[2] == 'KeyPress':
        letter = check_if_key_in_constants(lst[1])
        type(letter)
    else:
        coords_lst = lst[1].split(',')
        x_coord = int(coords_lst[0])
        y_coord = int(coords_lst[1])
        action = lst[2]
        path = makePath(lst[3])
        try:
            time.sleep(1)
            coords = find(path).getTarget()
            print('found icon')
        except:
            coords = Location(x_coord,y_coord)
            print('not found icon :(')
        acts[action](coords)


