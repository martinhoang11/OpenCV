import cv2
import numpy as np
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())


#load an image
image = cv2.imread(args['image'])
#cv2.imshow("Image", image)
#cv2.waitKey(0)

#convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray", gray)
#cv2.waitKey(0)

#edge detection
edged = cv2.Canny(gray, 30, 150)
#cv2.imshow("Edged", edged)
#cv2.waitKey(0)

#threshold
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
#cv2.imshow("Thresh", thresh)
#cv2.waitKey(0)


#find contours and draw
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
cnts = imutils.grab_contours(cnts)
print(np.array(cnts).shape)
output = image.copy()

#loop in contours
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
    cv2.imshow("Contours", output)
    cv2.waitKey(0)

#put some texts
text = "I found {} objects".format(len(cnts))
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 
        (240, 0, 159), 2)
cv2.imshow("Texts", output)
cv2.waitKey(0)

#erosions
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=10)
cv2.imshow("Eroded", mask)
cv2.waitKey(0)

#dilate
dilate = thresh.copy()
mask = cv2.dilate(dilate, None, iterations=5)
cv2.imshow("Dilated", dilate)
cv2.waitKey(0)

#bitwise
bitwise = thresh.copy()
output = cv2.bitwise_and(image, image, mask=bitwise)
cv2.imshow("Output", output)
cv2.waitKey(0)
