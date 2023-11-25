import cv2
num_down=2
num_bilateral=7
img_rgb= cv2.imread("kitten.jpg")

img_colour=img_rgb
#downsampling image
for _ in range(num_down):
    img_colour=cv2.pyrDown(img_colour)
    
#applying bilateral filter slowly
for _ in range(num_bilateral):
     img_colour=cv2.bilateralFilter(img_colour,9,9,7)
for _ in range(num_down):
    img_colour=cv2.pyrUp(img_colour) 

#convert to grayscale and aplly median blur
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)
img_bllur=cv2.medianBlur(img_gray,7)

#CREATE EDGE MASK
img_edge=cv2.adaptiveThreshold(img_bllur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)

#combine color image with edge mask
img_edge=cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
img_cartoon=cv2.bitwise_and(img_colour,img_colour,img_edge)

#display
cv2.namedWindow("cartoon",cv2.WINDOW_GUI_NORMAL)
cv2.imshow("cartoon",img_cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

