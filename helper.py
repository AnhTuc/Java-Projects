import cv2

import matplotlib.pyplot as plt
import numpy as np


def readImg(img_path, img_height = 160, img_width = 160):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, [img_height, img_width])
    return img

def show_img(img, title = None):
    plt.figure(figsize = (10,10))
    plt.imshow(img.astype('uint8'))
    plt.title(title)
