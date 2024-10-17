import cv2
import numpy as np
import matplotlib.pyplot as plt


#reading image
bact_img = cv2.imread("bacteria3.jpg")
#reading gray image
gray_img = cv2.cvtColor(bact_img,cv2.COLOR_BGR2GRAY)

assert bact_img is not None,"Image file not found. Check path os.path.exist"

#showing original and gray image
cv2.imshow("Original Image",bact_img)
cv2.imshow("Grayscale Image",gray_img)

#Applying Gaussian blur
blur_img = cv2.GaussianBlur(gray_img,(7,7),0.3)
cv2.imshow("Blurred Image",blur_img)

#Displaying Histogram
plt.hist(blur_img.ravel(), bins=256,range=(0,256))
plt.title("Bacteria Image Histogram using hist")
plt.xlabel('pixel values')
plt.ylabel('frequency')
plt.show()

#Creating a mask for the black spots on image
mask = blur_img < 20
plt.imshow(mask, cmap="gray")
plt.show()

mask = mask.astype(np.uint8)*255

#Finding contours of the spots
contour,hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
colored_img = np.zeros_like(bact_img)

#Iterated over the contours and assigned purple colour to each spot 
for cnt in contour:
  area = cv2.contourArea(cnt)
  cv2.drawContours(colored_img,[cnt],-1,(232, 8, 252),-1)
output_img = cv2.addWeighted(bact_img, 1, colored_img, 0.3, 0)

# Displaying the final image with colored spots
plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
plt.title("Colored Spots on Bacteria Colony")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()