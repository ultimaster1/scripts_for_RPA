import os
import time
import sys.argv


def check_if_key_in_constants(key):
    special_keys = {'tab': Key.TAB, 
         'backspace' : Key.BACKSPACE,
         'enter' : Key.ENTER,
         'esc' : Key.ESC,
         'delete' : Key.DELETE,
         'insert' : Key.INSERT,
         'space' : Key.SPACE
           }  
    try:
        special_key_arr = key.split('.')  
        key = special_key_arr[1]
    except:         
        pass
    key = key.replace("'","")
    if key in list(special_keys.keys()):
        return special_keys[key]
    else:
        return key


log_path = sys.argv[1]
dg = open(log_path,'r')
lines = dg.read().splitlines()
print(lines)
acts = {'Click' : click, 'DoubleClick' : doubleClick}
print(lines[0].split('|'))
for i in lines:
    lst = i.split('|')
    if lst[1] == 'KeyPress':
        letter = check_if_key_in_constants(lst[2])
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
