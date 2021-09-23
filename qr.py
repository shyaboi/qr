import pyqrcode
from numpy import random
import jwt


{'some': 'payload'}
tots = []
finalHash= ''

for x in range(13):
    
    tots.append({"user":"this is a typical sentence that people might send...",})
    print(tots)
    hashyBoi= jwt.encode({'arr':tots}, "secret", algorithm="HS256")
    finalHash = hashyBoi
    url = pyqrcode.create(str("http://localhost:5000/hB/"+hashyBoi))
    url.svg(f'hashedConv{x}.svg', scale=8)

deep = jwt.decode(finalHash, "secret", algorithms=["HS256"])
print(finalHash)
    # print(url.terminal(quiet_zone=1))