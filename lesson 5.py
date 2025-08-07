import cv2
#print(cv2.__version__)

image = cv2.imread('example.jpg')


cv2.namedWindow('Loaded image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded image', 800, 500)


cv2.imshow('Loaded image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


print(f"Image dimensions: {image.shape}")