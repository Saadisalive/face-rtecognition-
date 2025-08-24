import cv2

image = cv2.imread('Screenshot 2025-08-24 192833.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (800, 500))
cv2.imshow('Resized Grayscale Image', resized_image)
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('resized_grayscale_image.png', resized_image)
    print("Image saved as 'resized_grayscale_image.png'")
else:
    print("Image not saved.")

cv2.destroyAllWindows()
