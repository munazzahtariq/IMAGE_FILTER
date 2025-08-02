import cv2 as cv
#if you have a bigger than your screen the code automaticaaly resize it to half of its orignal size
#ADD OPTIONAL RESIZING
#ADD LOOP SO USERS CAN USE MORE THAN ONE FILTER
#ADD ARGPARSE DRAG AND DROP
#only blurring the bg


print("WELCOME TO IMAGE FILTER APP")
print("You can do the apply the following filters by pressing their serial number")
print("1. BLUR THE IMAGE")
print("2. SEE ONLY THE EDGES OF THE IMAGE")
print("3. BLUR BUT RETAIN THE EDGES THE IMAGE")
print("4. GRAYSCALE THE IMAGE")
print("5.CONVERSION FROM BGR TO HSV OR LAB OF THE IMAGE")
print("6.FACIAL DETECTION ON IMAGE")

img=input("Enter the path of your image").strip()
image=cv.imread(img) 
resize=cv.resize(image,(image.shape[1]//2,image.shape[0]//2))
cv.imshow("ORIGNAL IMAGE",resize)
x=int(input("Enter the serial number"))

if x==1:
    blur=cv.GaussianBlur(resize,(7,7),cv.BORDER_DEFAULT)
    cv.imshow("BLURRED IMAGE",blur)
    print("DONE")

elif x==2:
    canny=cv.Canny(resize,125,175)
    cv.imshow("CANNIED IMAGE",canny)
    print("DONE")

elif x==3:
    bilateral=cv.bilateralFilter(resize,10,35,10)
    cv.imshow("RETAINED EDGES",bilateral)
    print("DONE")

elif x==4:
    gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
    cv.imshow("GRAYSCALED IMAGE",gray)
    print("DONE")

elif x==5:
    y=int(input("Do you want to convert to HSV or LAB , enter 1 for hsv or 2 for lab"))
    if y==1:
        hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
        cv.imshow("HSV FORMAT",hsv)
        print("DONE")
    elif y==2:
        lab=cv.cvtColor(resize,cv.COLOR_BGR2Lab)
        cv.imshow("LAB FORMAT",lab)
        print("DONE")
    else:
        print("Invalid number")

elif x==6:
    gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("Gray",gray)
    haar_cascade=cv.CascadeClassifier("haar_face.xml")
    #changing the number will reduce noise in the image meaning if the stomach and neck is detected
    #then we can change the min neighbours
    face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    print(f"the number of faces are is {len(face_rect)}")
    for (x,y,w,h) in face_rect:
        cv.rectangle(image,(x,y),(x+w,y+h),(0,255,0),thickness=1)
    cv.imshow("Detected_face",image)


else:
    print("Invalid number")

print("PRESS ANY KEY TO CLOSE THE IMAGES")


cv.waitKey(0)
cv.destroyAllWindows()
    
        


