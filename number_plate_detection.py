import cv2 as c

nPlateCascade=c.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea=00
img1=c.imread("car1.jpg")
img2=c.imread("car2.jpg")
img3=c.imread("car3.jpg")
dimensions = (600,600)

#put the images you want to use where img1 is
img_to_use=img1
img = c.resize(img_to_use, dimensions, interpolation = c.INTER_AREA)

imgGray=c.cvtColor(img,c.COLOR_BGR2GRAY)
numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in numberPlates:
    area=w*h
    if area>minArea:
        c.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        c.putText(img,"Number plate",(x,y-10),c.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),2)
        imgRoi=img[y:y+h,x:x+w]
        c.imshow("Number PLate",imgRoi)

c.imshow("car1",img)
c.waitKey(0)
c.destroyAllWindows()