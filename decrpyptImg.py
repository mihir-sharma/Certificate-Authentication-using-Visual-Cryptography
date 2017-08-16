import numpy as np
import cv2
import json

keyServer = open("key.txt", "r")
shareCert = open("SC.txt", "r")

img = np.zeros((585,585,3), np.uint8)
img[:] = (255,255,255)
client = np.array(json.load(shareCert))
server = np.array(json.load(keyServer))
arr = []
for i in range(0,585):
    for j in range(0,585):
        b = int(client[585 * i + j][0] ^ server[585 * i + j][0])
        g = int(client[585 * i + j][1] ^ server[585 * i + j][1])
        r = int(client[585 * i + j][2] ^ server[585 * i + j][2])
        arr.append([b, g, r])
        img.itemset((i, j, 0), b)
        img.itemset((i, j, 1), g)
        img.itemset((i, j, 2), r)
cv2.imwrite("regenImg.png", img)
