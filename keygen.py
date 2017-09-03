import numpy as np
import json

def keygen(x):
    key = open(x, "w")
    x = np.random.randint(0, 256, (342225, 3))
    key.write(json.dumps(x.tolist()))
    key.close()
