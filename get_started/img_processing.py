import imutils
import cv2

img = cv2.imread('shapes.png')
(h, w, d) = img.shape

print(f'width= {w}, height= {h}, depth={d}')

#cv2.imshow("Image", img)
#cv2.waitKey(0)

roi = img[60:100, 150:160]
#cv2.imshow("ROI", roi)
#cv2.waitKey(0)

#resize img

#r = 300.0 / w
#dim = (300, int(h*r))
#resized = cv2.resize(img, dim)
#cv2.imshow("Resize", resized)
#cv2.waitKey(0)

#rotate
#center = (w // 2, h // 2)
#M = cv2.getRotationMatrix2D(center, -45, 1.0)
#0print(M)
#rotated = cv2.warpAffine(img, M, (w,h))
#cv2.imshow("Rotate", rotated)
#v2.waitKey(0)

#rotate with imutils

rotated = imutils.rotate_bound(img, 45)
#cv2.imshow("Imutils bound rotation", rotated)
#cv2.waitKey(0)


#blur image with gaussian
#blurred = cv2.GaussianBlur(img, (11,11), 0)
#cv2.imshow("Blurred", blurred)
#cv2.waitKey(0)


#draw rectangle
rec = img.copy()
cv2.rectangle(rec, (100,60), (250,160), (0, 0, 255), 2)
cv2.imshow("REC", rec)
cv2.waitKey(0)

#draw circle
cir = img.copy()
cv2.circle(cir, (100,60), 20, (0, 0, 255), 2)
cv2.imshow("CIR", cir)
cv2.waitKey(0)


#draw line
line = img.copy()
cv2.line(line, (60, 20), (300, 140), (0, 0, 255), 2)
cv2.putText(line, "OpenCV + test draw line", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Line", line)
cv2.waitKey(0)





