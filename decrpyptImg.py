import numpy as np
import cv2
import json

def decryptImg(x, y, w, UID):
    
    keyServer = open(x, "r")
    shareCert = open(y, "r")
    orig = cv2.imread(w, -1)
    width, height = orig.shape[:2]
    img = np.zeros((width, height, 3), np.uint8)
    img[:] = (255,255,255)
    client = np.array(json.load(shareCert))
    server = np.array(json.load(keyServer))
    arr = []
    for i in range(0,width):
        for j in range(0,height):
            b = int(client[height * i + j][0] ^ server[height * i + j][0])
            g = int(client[height * i + j][1] ^ server[height * i + j][1])
            r = int(client[height * i + j][2] ^ server[height * i + j][2])
            arr.append([b, g, r])
            img.itemset((i, j, 0), b)
            img.itemset((i, j, 1), g)
            img.itemset((i, j, 2), r)
    cv2.imshow('image', img)
    cv2.waitKey(0)
