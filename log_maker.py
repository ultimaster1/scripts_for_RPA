import pyscreenshot as ImageGrab
import mouse
import time
import math
import logging
i = 0
diag = 30
logging.basicConfig(filename='C:/Users/kir/Desktop/actions/log.txt',level=logging.INFO)
path_to_folder = 'C:/Users/kir/Desktop/actions/'
while True:
    x, y = mouse.get_position()
    if mouse.is_pressed(button='left'):
        i += 1
        x1 = int(round(x - math.sqrt((diag * diag) / 2),0))
        x2 = int(round(x + math.sqrt((diag * diag) / 2),0))
        y1 = int(round(y + math.sqrt((diag * diag) / 2),0))
        y2 = int(round(y - math.sqrt((diag * diag) / 2),0))
        im = ImageGrab.grab(bbox=(x1, y2,x2, y1))
        img_path = path_to_folder + str(i) + 'im.jpeg'
        im.save(img_path ,quality = 230)
        logging.info('|' + str(x)+ ','+ str(y) + '|' + 'Click' + '|' + img_path)
        time.sleep(0.1)
    # elif mouse_double_pressed:
    # elif keyboard_pressed()
