
import cv2
car = cv2.imread("is200.jpg")
car2 = cv2.imread("r34.jpg")

rs = cv2.resize(car2, (269,180))
cv2.imshow("screen", rs)
cv2.waitKey(0)

add = cv2.addWeighted(car, 1, rs, 0.5, 0)
cv2.imshow("screen2",add )
cv2.waitKey(0)

sub = cv2.subtract(car,rs)
cv2.imshow("screen3", sub)
cv2.waitKey(0)



ga = cv2.GaussianBlur(car, (11,11), 0, 0)
cv2.imshow("screen4", ga)
cv2.waitKey(0)
me = cv2.medianBlur(car,7)
cv2.imshow("screen5", me)
cv2.waitKey(0)
bb = cv2.bilateralFilter(car, 35, 250, 250)
cv2.imshow("screen6", bb)
cv2.waitKey(0)

import numpy
matrix = numpy.ones((11, 11), numpy.uint8)
erosion = cv2.erode(car, matrix)
cv2.imshow("screen7", erosion)
cv2.waitKey(0)

Is200 = cv2.copyMakeBorder(car, 10, 10, 100, 100, cv2.BORDER_CONSTANT)
cv2.imshow("screen8", Is200)
cv2.waitKey(0)