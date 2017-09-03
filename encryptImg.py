import numpy as np
import cv2
import json

def createUser(UID):
    name = input("Enter name of student")
    fname = UID + ".txt"
    f =open(UID + "/" + fname, 'w')
    details = {}
    details["UID"] = UID
    details["Name"] = name
    json.dump(details, f)
    f.close()


def encryptImg(x, y, z, w):
    keyServer = open(x, "r")
    shareCert = open(y, "w")

    x = np.array(json.load(keyServer))
    keyServer.close()

    img = cv2.imread(z, -1)
    arr = []
    for i in range(0, 585):
        for j in range(0, 585):
            b = int(img[i, j, 0] ^ x[585 * i + j][0])
            g = int(img[i, j, 1] ^ x[585 * i + j][1])
            r = int(img[i, j, 2] ^ x[585 * i + j][2])
            arr.append([b, g, r])

    shareCert.write(json.dumps(np.asarray(arr).tolist()))
    shareCert.close()

    imgshareClient = open(y, "r")
    img = np.zeros((585,585,3), np.uint8)
    img[:] = (255,255,255)
    y = np.array(json.load(imgshareClient))

    for i in range(0,585):
        for j in range(0,585):
            bl = y[i*585+j][0]
            gr = y[i*585+j][1]
            rd = y[i*585+j][2]
            img.itemset((i, j, 0), bl)
            img.itemset((i, j, 1), gr)
            img.itemset((i, j, 2), rd)
    cv2.imwrite(w, img)
