import DB_creator
import encryptImg
import decrpyptImg
import keygen
import fileMove
import getUserDetails

picker = int(input("1 for encrypt / 2 for decrypt        "))
if picker is 1:
    dirPath = getUserDetails.getUID()
    DB_creator.createDir(dirPath)
    encryptImg.createUser(dirPath)
    fileMove.fileMove(dirPath)
    keygen.keygen(dirPath + "/key.txt")
    encryptImg.encryptImg(dirPath + "/key.txt", dirPath + "/SC.txt", dirPath + "/imgDefault.png", dirPath + "/SC.png")

elif picker is 2:
    dirPath = getUserDetails.getUID()
    decrpyptImg.decryptImg(dirPath + "/key.txt", dirPath + "/SC.txt", dirPath + "/regenImg.png", dirPath + "/imgDefault.png", dirPath)
else:
    print("INVALID INPUT. Program terminated.")
