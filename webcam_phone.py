import cv2
import requests
import numpy as np
import imutils

# install IP webcam in your phone and copy that IP to this url.

url = "http://100.96.223.78:8080/shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=640)
    cv2.imshow("Mobile Webcam", img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
