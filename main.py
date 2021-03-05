import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api, win32con
import os

last_time = time.time()
path = os.getcwd()
kernel_path   = os.path.join(path, 'cir.png')
kernel = np.array(cv2.imread(kernel_path))
kernel = cv2.cvtColor(kernel, cv2.COLOR_BGR2GRAY)
kernel = kernel/(kernel.sum())                      # Kernel normalization

### Colorfull to grayScale --> Apply a threshold --> Convolutional filter --> Apply a threshold
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    ret, processed_img = cv2.threshold(processed_img, 250, 255, cv2.THRESH_BINARY)
    processed_img = cv2.filter2D(processed_img, -1, kernel)
    ret, processed_img = cv2.threshold(processed_img, 50, 255, cv2.THRESH_BINARY)
    return processed_img

### Click on screen
def click(x=480,y=480):
    #win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

### Decides when to click
 # If there were more than 10 white pixels in the image,
 # it means the ball is in the right position; so you
 # have to click on the screen.
def DoGame(screen):
    if screen.sum() > 10:
        click()
        print("clicked")
        #time.sleep(0.09)

### Countdown
def CountDown():
    for i in range(1,4)[::-1]:
        print(i)
        time.sleep(1)
    print("Running")

### Main
CountDown()
while(True):
    #screen = np.array(ImageGrab.grab(bbox=(1920/6,1080/8,1920/6*2,1080/2)))
    screen = np.array(ImageGrab.grab(bbox=(380,140,445,520)))
    new_screen = process_img(screen)

    DoGame(new_screen/255)
    print('Processing FPS: {}'.format(int(1/(time.time()-last_time))))
    last_time = time.time()

    ### Uncomment 4 lines below to see the prosecced image:
    # cv2.imshow('window', new_screen)
    # if cv2.waitKey(10) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break
