import win32api
import keyboard
import mouse
import math
import logging
import time
from threading import Thread
from pynput.keyboard import Listener
import os
from mss import mss
from PIL import Image

logging.basicConfig(filename='C:/Users/kir/Desktop/actions/log.txt',level=logging.INFO)


class Action_Logger():

    def __init__(self, diag = 30, path = 'C:/Users/kir/Desktop/actions/',state_left = 0):
        self.diag = diag
        self.path = path
        self.num = 0
        self.state_left = win32api.GetKeyState(0x01)
        self.img = 0

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
        bbox = (x1, y2, x2, y1)
        sct_img = mss().grab(bbox)
        im = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        return [im,x,y]

    def mouse_click(self):
        a = win32api.GetKeyState(0x01)
        cnt = 0
        if a != self.state_left:
            if a < 0:
                if self.img == 0:
                    self.img = self.image_bbox()
                else:
                    pass
            else:
                print('ds')
                try:
                    if self.img != 0:
                        print('teper tut')
                        img = self.img
                    else:
                        print('ne tut')
                        img = self.image_bbox()
                except:
                    print('problem')
                self.state_left = a
                cnt += 1
                x = time.time()
                while (time.time() - x) < 0.15:
                    b = win32api.GetKeyState(0x01)
                    if b != self.state_left:  # Button state changed
                        if b >= 0:
                            print('ya zdes')
                            self.state_left = abs(a - 1)
                            cnt += 1
                            self.num += 1
                            self.img = 0
                            return self.log_on(cnt, self.num, img[0], img[1], img[2])
                self.num += 1
                self.img = 0
                return self.log_on(cnt, self.num, img[0], img[1], img[2])



    # def mouse_click(self):
    #     a = win32api.GetKeyState(0x01)
    #     cnt = 0
    #     if keyboard.is_pressed('esc'):
    #         os._exit(0)
    #     if a != self.state_left:  # Button state changed
    #         if a >= 0:
    #             img = self.image_bbox()
    #             self.state_left = a
    #             cnt += 1
    #             x = time.time()
    #             while (time.time() - x) < 0.5:
    #                 b = win32api.GetKeyState(0x01)
    #                 if b != self.state_left:  # Button state changed
    #                     if b >= 0:
    #                         self.state_left = abs(a - 1)
    #                         cnt += 1
    #                         self.num += 1
    #                         # print(img)
    #                         return self.log_on(cnt, self.num,img[0],img[1],img[2])
    #             self.num += 1
    #             return self.log_on(cnt, self.num,img[0],img[1],img[2])


def on_press(key):  # The function that's called when a key is pressed
    logging.info("|KeyPress|{0}".format(key))

def key_loop():
    with Listener(on_press=on_press) as listener:  # Create an instance of Listener
        listener.join()  # Join the listener thread to the main thread to keep waiting for keys


def mouse_loop(obj):
    while True:
        obj.mouse_click()


if __name__ == "__main__":
    print('add path to')
    A_L = Action_Logger()
    keyboard_th = Thread(target=key_loop)
    mouse_th = Thread(target=mouse_loop,args=(A_L,))
    keyboard_th.start()
    mouse_th.start()
