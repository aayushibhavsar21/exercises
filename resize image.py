print("_______resize image_______")

import cv2
image=cv2.imread("FluorescentCells.jpg",cv2.IMREAD_UNCHANGED)
cv2.imshow("title",image)
cv2.waitKey(0)

width=int(image.shape[1]*50/100)
height=int(image.shape[0]*50/100)

output=cv2.resize(image , (width,height) )

cv2.imwrite("newimage.jpg",output)
cv2.waitKey(0)