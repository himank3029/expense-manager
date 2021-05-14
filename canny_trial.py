import cv2
import numpy as np
def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged

image = cv2.imread("bbill.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
# apply Canny edge detection using a wide threshold, tight
# threshold, and automatically determined threshold
wide = cv2.Canny(blurred, 10, 20)
tight = cv2.Canny(blurred, 225, 250)
auto = auto_canny(blurred)
# show the images
cv2.imshow("Original", image)
cv2.imshow("Edges", np.hstack([wide, tight, auto]))
cv2.imshow("auto",auto)
cv2.waitKey(0)

new = cv2.Canny(gray, 10, 50)
cv2.imshow("new",new)
cv2.waitKey(0)
