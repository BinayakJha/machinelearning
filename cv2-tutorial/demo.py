import cv2

img1 = cv2.imread('https://pandas.pydata.org/pandas-docs/stable/_images/pandas-DataFrame-hist-1.png')


cv2.imshow('original',img1)
cv2.waitKey()
cv2.destroyAllWindows()