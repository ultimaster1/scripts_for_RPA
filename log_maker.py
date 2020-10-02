import win32api
import pyscreenshot as ImageGrab
import mouse
import math
import logging
import keyboard
import string
import time


# num = 0
# diag = 30
# path_to_folder = 'C:/Users/kir/Desktop/actions/'
# alphabet_string = string.ascii_lowercase
# alphabet = list(alphabet_string)
# special_combinations = ['space','ctrl+shift','capslock','alt+shift','backspace','enter']
# alphabet_shift = list(map(shif_plus,alphabet))
# all_keys = alphabet + special_combinations
# all_keys_shif = alphabet_shift + special_combinations
# state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128


def shif_plus(x):
    return 'shift+' + x

logging.basicConfig(filename='C:/Users/kir/Desktop/actions/log.txt',level=logging.INFO)


class Action_Logger():
    def __init__(self, diag = 30, path = 'C:/Users/kir/Desktop/actions/'):
        self.diag = diag
        self.path = path
        self.num = 0
        self.state_left = win32api.GetKeyState(0x01)


    def log_on(self, number_of_clicks,number_of_image,im = 0,x= 0,y= 0):
        if number_of_clicks == 1:
            clicktype = 'Click'
        else:
            clicktype = 'DoubleClick'
        img_path = self.path + str(number_of_image) + 'im.jpeg'
        im.save(img_path, quality=230)
        logging.info('|' + str(x) + ',' + str(y) + '|' + clicktype + '|' + img_path)
        print(clicktype)
        print(number_of_image)

    def image_bbox(self):
        x, y = mouse.get_position()
        x1 = int(round(x - math.sqrt((self.diag * self.diag) / 2), 0))
        x2 = int(round(x + math.sqrt((self.diag * self.diag) / 2), 0))
        y1 = int(round(y + math.sqrt((self.diag * self.diag) / 2), 0))
        y2 = int(round(y - math.sqrt((self.diag * self.diag) / 2), 0))
        im = ImageGrab.grab(bbox=(x1, y2, x2, y1))
        return [im,x,y]

    def mouse_click(self):
        a = win32api.GetKeyState(0x01)
        cnt = 0
        if a != self.state_left:  # Button state changed
            if a >= 0:
                img = self.image_bbox()
                self.state_left = a
                cnt += 1
                x = time.time()
                while (time.time() - x) < 0.15:
                    b = win32api.GetKeyState(0x01)
                    if b != self.state_left:  # Button state changed
                        if b >= 0:
                            self.state_left = abs(a - 1)
                            cnt += 1
                            self.num += 1
                            # print(img)
                            return self.log_on(cnt, self.num,img[0],img[1],img[2])
                self.num += 1
                return self.log_on(cnt, self.num,img[0],img[1],img[2])



if __name__ == "__main__":
    alphabet = list(string.ascii_lowercase) + ['space', 'ctrl+shift', 'capslock', 'alt+shift', 'backspace', 'enter',
                                               'esc']
    alphabet_shift = list(map(shif_plus, alphabet)) + ['space', 'ctrl+shift', 'capslock', 'alt+shift', 'backspace',
                                                       'enter','esc']
    A_L = Action_Logger()
    while True:
        A_L.mouse_click()
        for i in alphabet:
            if keyboard.is_pressed(i):
                logging.info('|' + i + '|' + 'KeyPress')
                time.sleep(0.25)
            elif keyboard.is_pressed('shift'):
                for k in alphabet_shift:
                    if keyboard.is_pressed(k):
                        up = k.split('+')[1].upper()
                        logging.info('|' + up + '|' + 'KeyPress')

