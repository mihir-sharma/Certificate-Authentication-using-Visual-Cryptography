#   import dependencies
import numpy as np      #   Numpy is used to create a random Nd array
import json             #   Json library is included to store data in Json format

#   create file for storing key
key = open("key.txt", "w")

#   Create a nX3 array of random integers in range 0 to 255.
#   Here n is the total number of pixels in the image to be encrypted.
x = np.random.randint(0, 256, (342225, 3))

#   Dump created nX3 array into file created. The data is stored in Json format.
key.write(json.dumps(x.tolist()))

#   Close file
key.close()
