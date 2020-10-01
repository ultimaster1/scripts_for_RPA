import os
import time
log_path = 'C:/Users/kir/Desktop/actions/log.txt' # Путь к файлу логов
dg = open(log_path,'r')
lines = dg.read().splitlines()
acts = {'Click' : click, 'DoubleClick' : doubleClick}  # Список функций и подходящих под них функций
for i in lines:
    lst = i.split('|')
    coords_lst = lst[1].split(',')
    x_coord = int(coords_lst[0])
    y_coord = int(coords_lst[1])
    action = lst[2]
    path = makePath(lst[3])
    try:
        time.sleep(1)
        coords = find(path).getTarget()
        print('found icon') # Если координаты иконки найдены 
    except:
        coords = Location(x_coord,y_coord)
        print('not found icon :(') # Если координаты иконки не найдены (тогда ориентируется по коориднатам из лог файла)
    acts[action](coords)
