import cv2
import os

def overlay_images():
    for i in range(100000):
        if os.path.isfile("figure_captured_{}.png".format(i)):
            im_gray = cv2.imread('figure_captured_{}.png'.format(i), cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            cv2.imwrite('figure_captured_{}.png'.format(i), im_bw)
            print("image exist ",i)
        else:
            print("loops braks here ",i)
            break
   
    
    for i in range(1,10000):
        if os.path.isfile("figure_captured_{}.png".format(i)):    
            if i==1:
                print(i,i-1)
                img1=cv2.imread("figure_captured_{}.png".format(i-1))
                img2=cv2.imread("figure_captured_{}.png".format(i))
                img_temp = cv2.addWeighted(img1,0.5,img2,0.5,0)
                im_gray = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
                (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                cv2.imwrite("super_imposed.png",im_bw)
                
            else:
                img1=cv2.imread("figure_captured_{}.png".format(i))
                img2=cv2.imread("super_imposed.png")
                img_temp = cv2.addWeighted(img1,0.5,img2,0.5,0)
                im_gray = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)
                (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
                cv2.imwrite("super_imposed.png",im_bw)
                print("image exist ",i)
        else:
            print("loops braks here ",i)
#            cv2.imshow("Super imposed image",im_bw)
#            cv2.waitKey(0)
#            cv2.destroyAllWindows()
            for i in range(10000):
                 if os.path.isfile("figure_captured_{}.png".format(i)):
                     print("yes")
                     os.remove("figure_captured_{}.png".format(i))
                 else:
                    break
            break
        
    
#overlay_images()





##originalImage = cv2.imread('check.png')
##grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
##  
##(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY| cv2.THRESH_OTSU)
## 
##cv2.imshow('Black white image', blackAndWhiteImage)
##cv2.imshow('Original image',originalImage)
##cv2.imshow('Gray image', grayImage)
##  
##cv2.waitKey(0)
##cv2.destroyAllWindows()
#
#
#
#img1 = cv2.imread('figure_captured_0.png')
#img2 = cv2.imread('figure_captured_1.png')
#
##img2 = cv2.imread('figure_captured_1.png')
##img3 = cv2.imread('figure_captured_2.png')
##img4 = cv2.imread('figure_captured_3.png')
##img5 = cv2.imread('figure_captured_4.png')
##img6 = cv2.imread('figure_captured_5.png')
##img7 = cv2.imread('figure_captured_6.png')
##img8 = cv2.imread('figure_captured_7.png')
##img9 = cv2.imread('figure_captured_9.png')
#
#
#dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
##dst = cv2.addWeighted(dst,0.5,img3,0.3,0)
##dst = cv2.addWeighted(dst,0.5,img4,0.3,0)
##dst = cv2.addWeighted(dst,0.6,img5,0.3,0)
###dst = cv2.addWeighted(dst,0.7,img6,0.4,0)
###dst = cv2.addWeighted(dst,0.7,img7,0.4,0)
###dst = cv2.addWeighted(dst,0.7,img8,0.4,0)
####dst = cv2.addWeighted(dst,0.7,img9,0.4,0)
#
#
##
##cv2.imshow('dst',dst)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
#cv2.imwrite("check.png",dst)
#
#
#
#
#
#from PIL import Image
#
#col = Image.open("figure_captured_1.png")
#gray = col.convert('L')
#bw = gray.point(lambda x: 0 if x<128 else 255, '1')
#bw.save("result_bw_2.png")
#
#
#import cv2
#
##-----Reading the image-----------------------------------------------------
#img = cv2.imread('Dog.jpg', 1)
#cv2.imshow("img",img) 
#
##-----Converting image to LAB Color model----------------------------------- 
#lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow("lab",lab)
#
##-----Splitting the LAB image to different channels-------------------------
#l, a, b = cv2.split(lab)
#cv2.imshow('l_channel', l)
#cv2.imshow('a_channel', a)
#cv2.imshow('b_channel', b)
#
##-----Applying CLAHE to L-channel-------------------------------------------
#clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
#cl = clahe.apply(l)
#cv2.imshow('CLAHE output', cl)
#
##-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
#limg = cv2.merge((cl,a,b))
#cv2.imshow('limg', limg)
#
##-----Converting image from LAB Color model to RGB model--------------------
#final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
#cv2.imshow('final', final)
#
#
