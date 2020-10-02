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


    def log_on(self, number_of_clicks,number_of_image):
        if number_of_clicks == 1:
            clicktype = 'Click'
        else:
            clicktype = 'DoubleClick'

        x, y = mouse.get_position()
        number_of_image += 1
        x1 = int(round(x - math.sqrt((self.diag * self.diag) / 2), 0))
        x2 = int(round(x + math.sqrt((self.diag * self.diag) / 2), 0))
        y1 = int(round(y + math.sqrt((self.diag * self.diag) / 2), 0))
        y2 = int(round(y - math.sqrt((self.diag * self.diag) / 2), 0))
        im = ImageGrab.grab(bbox=(x1, y2, x2, y1))
        img_path = self.path + str(number_of_image) + 'im.jpeg'
        im.save(img_path, quality=230)
        logging.info('|' + str(x) + ',' + str(y) + '|' + clicktype + '|' + img_path)
        time.sleep(0.25)


    def image_bbox(self):
        x, y = mouse.get_position()
        x1 = int(round(x - math.sqrt((self.diag * self.diag) / 2), 0))
        x2 = int(round(x + math.sqrt((self.diag * self.diag) / 2), 0))
        y1 = int(round(y + math.sqrt((self.diag * self.diag) / 2), 0))
        y2 = int(round(y - math.sqrt((self.diag * self.diag) / 2), 0))
        im = ImageGrab.grab(bbox=(x1, y2, x2, y1))
        return im

    def mouse_click(self):
        a = win32api.GetKeyState(0x01)
        cnt = 0
        if a != self.state_left:  # Button state changed
            self.num += 1
            if a < 0:
                # self.image_bbox()
                print('botton pressed')
            if a >= 0:
                cnt += 1
                print('botton unpressed')
                self.state_left = win32api.GetKeyState(0x01)
                x = time.time()
                while (time.time() - x) < 0.15:
                    a = win32api.GetKeyState(0x01)
                    if a != self.state_left:  # Button state changed
                        self.state_left = a
                        if a < 0:
                            print('botton preesed again')
                        if a >= 0:
                            print('botton unpreesed again')
                            cnt += 1
                            return self.log_on(cnt, self.num)
                return self.log_on(cnt, self.num)





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

        time.sleep(0.001)
