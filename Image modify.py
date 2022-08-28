import cv2
path = r"D:\Python Projects\OpenCV\image_1.jpg"
img = cv2.imread(path) # Read IMG file
cv2.imshow('Xem Anh',img) # Show IMG file


cv2.waitKey(0)